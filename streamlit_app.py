import streamlit as st  # ✅ import ก่อน
from chatbot import chatbot

st.set_page_config(page_title="My Portfolio", page_icon="🎨", layout="wide")

def chat_with_llm(user_input):
    return "Hello! How can I assist you?"  

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Chatbot", "Contact"])

if page == "Home":
    st.title("🚀 Welcome to My Portfolio Website")
    st.write("")
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image("./asset/Me.png")

    with col2:
        
        st.header("About Me", divider='gray')
        st.write("""
            Fourth-year Engineering student with a passion for programming 💻. I have experience in developing front-end (React) ⚛️ and backend (Node.js) 🔧 development, as well as Mobile Applications (Flutter) 📱. Additionally, I have worked on Deep Learning projects and am familiar with various tools for Deep Learning and image processing, such as OpenCV, TensorFlow, and YOLO. Skilled in model training and optimization.
        """)
        
        st.subheader("Tech Stack", divider="gray")
        
        Programming_Languages = ["HTML", "CSS", "PHP" ,"JavaScript", "TypeScript" , "Go" , "Python", "Java", "Dart"]
        selection = st.pills("Programming Languages", Programming_Languages, selection_mode="single")
        
        Framework = ["Bootstrap", "Tailwind", "React" ,"Node.js", "Fiber" , "Flask" , "Flutter"]
        selection = st.pills("Framework", Framework, selection_mode="single")
                
        Tools = ["Git", "Postman", "Docker" ,"AWS"]
        selection = st.pills("Tools", Tools, selection_mode="single")

elif page == "Projects":
    st.header("My Projects")
    projects = [
        {"title": "Job Matching System", "desc": "A job-matching platform using AI."},
        {"title": "OCR License Plate Recognition", "desc": "A deep learning-based OCR for license plates."},
        {"title": "E-commerce Website", "desc": "A full-stack online shopping platform."}
    ]
    for project in projects:
        st.subheader(project["title"])
        st.write(project["desc"])
        st.divider()

elif page == "Chatbot":
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.header("💬 Chat with AI to know more about me!")
    st.write("")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        response = chatbot(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            st.write(response)

elif page == "Contact":
    st.header("📬 Contact Me")
    st.write("Feel free to reach out to me via email or LinkedIn.")
    st.write("📧 Email: phong.janjamsai@gmail.com")
    st.write("🔗 LinkedIn: [My Profile](https://www.linkedin.com/in/phongsathorn-janjamsai-128184259)")
