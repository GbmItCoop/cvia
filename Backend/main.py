import sys
import os
# Add the path to the root directory of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import os
from Backend.match_resume_offer import evaluate_resumes

# Opening JSON file
f = open('Backend/config.json')
conf = json.load(f)


apikey = conf["api-key" ]
directory = "C:/Users/sofia/OneDrive/Bureau/teste"
# Example usage:
resumes = []
#job_offer_text = "Vous êtes diplômé d’un Bac+5 avec une spécialisation en informatique dans le domaine décisionnelle.Vous disposez d’une expérience de minimum 7 ans sur ce type de poste.Vous possédez des bases solides en modélisation (dimensionnelle, relationnelle), bases de données Oracle, en data visualisation (Qlik Sense/Cloud) et en solutions cloud data (Notions AWS, Azure, Oracle ou autre).Travailler en mode Agile n’a plus de secret pour vous.Autonome et proactif, vous êtes reconnu pour votre sens du service client, votre rigueur, votre sens de l’analyse et votre capacité à gérer des projets de dimension variable. Doté d’un bon relationnel, vous appréciez travailler en équipe et aimer travailler dans un environnement en constante évolution"

#job_offer_text ="Compétences :- Graphisme, Wordpress - Réseaux sociaux - Pack Office Qualités : - Créativité, dynamisme, force de proposition - Autonomie et rigueur - Excellente qualité rédactionnelle et expression orale"

job_offer_text = "Formation : Titulaire d'un BAC+2/+3 dans le domaine commercial B to B.Spécialisation : Expérience dans le secteur de la communication/publicité, notamment en régies, agences de publicité ou évènementielles Permis B exigé Compétences comportementales attendues : Aisance relationnelle, orientation client, très bonne communication orale, adaptabilité, sens de l’organisation, travail en équipe.Compétences techniques attendues : Techniques de vente et de négociation, stratégie de prospection commerciale, connaissance des espaces publicitaires web, supports et outils, identifier et exploiter les opportunités commerciales, outils bureautiques, outils collaboratifs… Process de recrutement Pré-qualification téléphonique Entretien managerEntretien Directeur de la Publicité + DRH"


aggregation_method = "mean"  # Or choose another method from the options
resumes_directory = "C:/Users/sofia/OneDrive/Bureau/teste"
for filename in os.scandir(resumes_directory):
    resumes.append(filename)



def main(resumes, job_offer_text,apikey , aggregation_method):
    best_resumes = evaluate_resumes(resumes, job_offer_text,apikey , aggregation_method)

    print(f"Best resumes based on {aggregation_method} aggregation:")
    for resume in best_resumes:
        print(resume)

if __name__ == '__main__':
    main(resumes, job_offer_text,apikey , aggregation_method)