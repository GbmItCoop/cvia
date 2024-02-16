import sys
import os
# Add the path to the root directory of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, jsonify, send_file
from Backend.match_resume_offer import evaluate_resumes
import os
import shutil

app = Flask(__name__)

# Assuming Backend is a package with __init__.py
from Backend import match_resume_offer

# Specify the directory where temporary resumes will be saved
temp_resumes_directory = 'C:\\tempcvia'

if not os.path.exists(temp_resumes_directory):
    os.makedirs(temp_resumes_directory)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    resumes = request.files.getlist('resumes')
    job_offer_text = request.form.get('jobOfferText', '')

    # Clear the content of the temporary resumes directory
    for file in os.listdir(temp_resumes_directory):
        file_path = os.path.join(temp_resumes_directory, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    # Save resumes temporarily and get their file paths
    resume_paths = []
    for resume in resumes:
        resume_path = os.path.join(temp_resumes_directory, resume.filename)
        resume.save(resume_path)
        resume_paths.append(resume_path)

    # Add your API key and aggregation method here
    apikey = "nbOKDe2YAM84Kh8B0UJ3sPGsDYXXg5NS"
    aggregation_method = "mean"

    best_resumes = evaluate_resumes(resume_paths, job_offer_text, apikey, aggregation_method)

    # Return the best matched resume
    return jsonify({'bestResume': best_resumes[0] if best_resumes else None})

@app.route('/download')
def download():
    best_resume = request.args.get('resume')

    if best_resume:
        best_resume_path = os.path.join(temp_resumes_directory, best_resume)
        print(best_resume)
        # Return the best-matched resume for download
        return send_file(best_resume_path, as_attachment=True, download_name=best_resume)
    else:
        return jsonify({'error': 'No best resume specified'})



#from waitress import serve

if __name__ == '__main__':
    # Use Waitress as the server instead of the built-in Flask server
    #serve(app, host='0.0.0.0', port=5000)
    app.run(debug=True)