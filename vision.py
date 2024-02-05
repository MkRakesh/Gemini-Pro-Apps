from dotenv import load_dotenv
load_dotenv() # load env variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def geminiResponse(input, image):
    
    if input != '':
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title = 'Gemini Vision')
st.title('Gemini Image Descriptor')

input = st.text_input('Input', key = 'input')

imageUploaded = st.file_uploader("choose an image...", type=["jpg", "jpeg","png"])

image = ''

if imageUploaded is not None:
 
    image = Image.open(imageUploaded)
    st.image(image, caption= "Uploaded Image", use_column_width = True)
    
submit = st.button("Describe image")

response = geminiResponse(input, image)

st.subheader('The response is')
st.write(response) 

