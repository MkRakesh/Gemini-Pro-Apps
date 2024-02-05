
from dotenv import load_dotenv
load_dotenv() # load env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


# function to load gemini response

def geminiResponse(query):
    
    response =  model.generate_content(query)
    return response.text
    
# st.set_page_config(page_title = 'Q&A')
st.title('Gemini LLM application')

input = st.text_input('Input', key = 'input')
submit = st.button('Pass your querry')

if submit:
    
    response = geminiResponse(input)
    st.subheader('The response is')
    st.write(response) 


    


