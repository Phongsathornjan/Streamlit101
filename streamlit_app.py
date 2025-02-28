import streamlit as st
# import pandas as pd

st.title('Show Dataset Web app')

st.sidebar.subheader('Input')
url_input = st.sidebar.text_input("Raw Dataset form github")

if(url_input):
    st.subheader('Output')
    st.info(f"The url of your data is {url_input}")
else:
    st.error("please enter your input")

