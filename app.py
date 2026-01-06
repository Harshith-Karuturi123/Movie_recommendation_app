import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

load_dotenv() #active api key

# Movie Recomendation System
st.title("🍿🎥✮⋆Movie Recomendation System 🍿🎥✮⋆ ")

user_input=st.text_input("Enter the Movie Name")
submit=st.button("Click here.....")

#if submit and user_input.strip():
#    st.markdown('Movie name has been entered')
#else:
#    st.warning('Enter the movie name')

model = genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip():
    st.markdown(f"Movie name entered:{user_input}")
    response = model.generate_content(f"Generate Movie Recommendations related to:{user_input}")
    st.write(f"related Recommendations for the similar movies: \n {response.text}")

else:
    st.write("You need to enter the movie name")