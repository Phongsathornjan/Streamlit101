import google.generativeai as genai
from dotenv import load_dotenv
import os

from read_pdf import read_pdf
Resume = read_pdf("Myinformation/Resume.pdf")
My_old_resume = read_pdf("Myinformation/My_old_resume.pdf")
Transcript = read_pdf("Myinformation/Transcript.pdf")
MyThesis = read_pdf("Myinformation/MyThesis.pdf")

load_dotenv()
api_key = os.getenv("Gemini_Key")
genai.configure(api_key=api_key)

def chatbot(chatHistory,user_input):
    prompt = f"""
    You are my AI assistant for my personal portfolio website.
    and when someone asked Who are you? you have to present yourself as my ai assistant.
    Your job is to answer questions about my background, projects, and skills.
    
    Here is my information
    My Resume :
    {Resume}
    
    My old Resume :
    {My_old_resume}
    
    Transcript :
    {Transcript}
    
    MyThesis :
    {MyThesis}
    
    chat history :
    {chatHistory}
    
    User Question: {user_input}
    
    
    """
    model = genai.GenerativeModel("gemini-1.5-flash")  
    response = model.generate_content(prompt)
    return response.text 
