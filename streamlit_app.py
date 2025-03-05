import streamlit as st  # ✅ import ก่อน

st.set_page_config(page_title="My Portfolio", page_icon="🎨", layout="wide")

def chat_with_llm(user_input):
    return "Hello! How can I assist you?"  

st.title("🚀 Welcome to My Portfolio Website")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Chatbot", "Contact"])

if page == "Home":
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
    st.header("💬 Chat with AI")
    user_input = st.text_input("Ask me anything:", "Hello!")
    if st.button("Send"):
        response = chat_with_llm(user_input)
        st.write("🤖 AI:", response)

elif page == "Contact":
    st.header("📬 Contact Me")
    st.write("Feel free to reach out to me via email or LinkedIn.")
    st.write("📧 Email: phong.janjamsai@gmail.com")
    st.write("🔗 LinkedIn: [My Profile](https://www.linkedin.com/in/phongsathorn-janjamsai-128184259)")
