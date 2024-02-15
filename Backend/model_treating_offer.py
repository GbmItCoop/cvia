from transformers import pipeline

def Funct_offer_treatement(sequence, cv_skills):
    try:
        classifier = pipeline("zero-shot-classification",
                               model="facebook/bart-large-mnli")

        sequence_to_classify = sequence
        candidate_labels = cv_skills
        result = classifier(sequence_to_classify, candidate_labels, multi_label=True)

        # Extracting and printing labels
        labels = result['labels']
        #print("Predicted Labels:", labels)

        # You can also print the scores if needed
        scores = result['scores']
        #print("Scores:", scores)
        return scores  # Return the match value
    except Exception as e:
        print(f"Error: {e}")
        return  0  # Return  0 if there is an exception


"""sequence = "Vous êtes diplômé d’un Bac+5 avec une spécialisation en informatique dans le domaine décisionnelle.Vous disposez d’une expérience de minimum 7 ans sur ce type de poste.Vous possédez des bases solides en modélisation (dimensionnelle, relationnelle), bases de données Oracle, en data visualisation (Qlik Sense/Cloud) et en solutions cloud data (Notions AWS, Azure, Oracle ou autre).Travailler en mode Agile n’a plus de secret pour vous.Autonome et proactif, vous êtes reconnu pour votre sens du service client, votre rigueur, votre sens de l’analyse et votre capacité à gérer des projets de dimension variable. Doté d’un bon relationnel, vous appréciez travailler en équipe et aimer travailler dans un environnement en constante évolution"
cv_skills = ['Cloud', 'Automation', 'R', 'Sql', 'P', 'Aws', 'Nosql', 'Communication', 'Python', 'Finance', 'C', 'Api', 'Etl', 'Crm']
Funct_offer_treatement(sequence, cv_skills)"""