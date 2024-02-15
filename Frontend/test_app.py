# test_app.py
import pytest
from app import analyze_job_offer, parse_resumes, prepare_matched_resume

# Test de la fonction analyze_job_offer
def test_analyze_job_offer():
    text = "We are looking for a Python developer with Flask experience in San Francisco."
    expected_result = {'skills': ['Python', 'Flask'], 'location': 'San Francisco'}
    assert analyze_job_offer(text) == expected_result

# Test de la fonction parse_resumes
def test_parse_resumes():
    # Création d'un faux objet fichier pour simuler le téléchargement d'un CV
    class FakeFile:
        def __init__(self, filename):
            self.filename = filename

    # Liste des fichiers de CV simulés
    files = [FakeFile('resume1.pdf'), FakeFile('resume2.pdf'), FakeFile('resume3.pdf')]
    expected_skills = ['Python', 'Java', 'Machine Learning']  # Les compétences extraites attendues

    assert parse_resumes(files) == expected_skills

# Test de la fonction prepare_matched_resume
def test_prepare_matched_resume(tmp_path):  # Utilisez tmp_path pour accéder au chemin temporaire du test
    # On crée un faux fichier pour simuler le CV correspondant
    fake_resume_content = b"This is a fake resume content."
    fake_resume_file = tmp_path / "matched_resume.pdf"
    fake_resume_file.write_bytes(fake_resume_content)

    ## Placeholder for the actual logic to find the best match and prepare the download
def prepare_matched_resume(skills, location):
    # On suppose que le chemin du fichier temporaire est généré de manière dynamique dans le test
    # Pour cet exemple, nous retournons simplement le chemin du fichier temporaire
    return str(tmp_path / "matched_resume.pdf")  # Utilisez tmp_path pour accéder au chemin temporaire du test

