import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("Gemini_Key")
genai.configure(api_key=api_key)

def chatbot(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")  
    response = model.generate_content(user_input)
    return response.text 

