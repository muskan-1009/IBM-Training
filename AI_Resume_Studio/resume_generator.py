import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_resume(name, education, skills, experience, job_role):
    prompt = f"""
    Generate a professional resume summary.

    Name: {name}
    Education: {education}
    Skills: {skills}
    Experience: {experience}
    Job Role: {job_role}

    Write a professional resume summary in 150-200 words.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text