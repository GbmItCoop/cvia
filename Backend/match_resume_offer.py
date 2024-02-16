import os
from functools import partial
from Backend.cv_resume_extractor import Funct_resume_extractor
from Backend.model_treating_offer import Funct_offer_treatement

def calculate_file_score(skill_scores, threshold=0.5, aggregation_method="mean"):
  """
  Calculates a file-level score based on individual skill scores.

  Args:
    skill_scores (list): A list of scores for each skill in the resume.
    threshold (float, optional): Minimum score to consider. Defaults to 0.5.
    aggregation_method (str, optional): Method to combine scores. Defaults to "mean".

  Returns:
    float: The combined file score.
  """

  filtered_scores = [score for score in skill_scores if score > threshold]

  if not filtered_scores:
    return 0  # Return 0 for no scores above threshold

  if aggregation_method == "mean":
    return sum(filtered_scores) / len(filtered_scores)
  else:
    raise ValueError(f"Invalid aggregation method: {aggregation_method}")

def evaluate_resumes(resumes, job_offer, apikey, aggregation_method):
  """
  Evaluates a list of resumes and returns the best ones based on skill matching scores.

  Args:
    resumes (list): A list of resume files or paths.
    job_offer (str): The text of the job offer.
    aggregation_method (str): Method to calculate file score.

  Returns:
    list: A list of the best resume files or paths.
  """

  scored_resumes = []
  for resume in resumes:
    skill_scores = Funct_offer_treatement(job_offer, Funct_resume_extractor(resume, apikey))
    file_score = calculate_file_score(skill_scores, aggregation_method=aggregation_method)
    scored_resumes.append((resume, file_score))

  scored_resumes.sort(key=lambda x: x[1], reverse=True)

  best_resumes = scored_resumes[:1][0]
  return best_resumes


