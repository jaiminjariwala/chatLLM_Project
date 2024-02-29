# import dotenv
from dotenv import load_dotenv

load_dotenv()   # load all env. variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# set api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# initialize our "Vision" model
model=genai.GenerativeModel("gemini-pro-vision")

# Function to load Gemini Pro Vision model and get responses
def get_gemini_response(input, image):
    # if there present any text input besides image, then generate both
    if input!= "":  
        response=model.generate_content([input, image])
    else:
        response=model.generate_content(image)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="Gemini Vision")
st.header("Chat Vision")
st.subheader("Gemini Powered Image to Text Conversational chatbot")

# create a input textbox
input = st.text_input("Enter Prompt",key="input")

# create image/file upload option
uploaded_file = st.file_uploader("Choose an image...",
                                 type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# create a submit button
submit=st.button("Tell me about the image")

# if submit is clicked...
if submit:
    response=get_gemini_response(input, image)

    # to print the response
    st.subheader("About Image:")
    st.write(response)
