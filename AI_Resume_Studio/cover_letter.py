import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_cover_letter(name, education, skills, experience, job_role):
    prompt = f"""
    Write a professional cover letter.

    Name: {name}
    Education: {education}
    Skills: {skills}
    Experience: {experience}
    Job Role: {job_role}

    Keep it professional and around 250 words.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text