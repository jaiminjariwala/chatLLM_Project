# import dotenv
from dotenv import load_dotenv

load_dotenv()   # loads all env. variables

import streamlit as st
import os
import google.generativeai as genai

# to set api key...
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# initialize our "language" model
model=genai.GenerativeModel("gemini-pro")

# Function to load Gemini Pro model and get responses
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="chatLLM")
st.header("Gemini LLM")

# create a textbox
input=st.text_input("Input:",key="input")

# create a submit button
submit=st.button("Ask the question")

# When submit is clicked...
if submit:
    response=get_gemini_response(input)

    # to print the response
    st.subheader("The Response is")
    st.write(response)
