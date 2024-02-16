import requests

def Funct_resume_extractor(directory, apikey):
    url = 'https://api.apilayer.com/resume_parser/upload'
    headers = {
        'Content-Type': 'application/octet-stream',
        'apikey': apikey
    }

    with open(directory, 'rb') as file:
        file_content = file.read()

    response = requests.post(url, headers=headers, data=file_content)

    # Check if the request was successful (status code  200)
    if response.status_code ==  200:
        result = response.json()  # Assuming the response is in JSON format
        print(f"resultats {result}\n")
        return result.get('skills', [])  # Ensure a list is returned even if 'skills' is missing
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []  # Return an empty list if the request fails

"""directory = "C:/Users/sofia/OneDrive/Bureau/teste/Graphiste.pdf"
apikey = "sh4ZYgLFRZmWEvnNx8S2AoXT7b2SIqJZ"
print(Funct_resume_extractor(directory, apikey))"""