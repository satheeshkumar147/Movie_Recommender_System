import streamlit as st
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import warnings
warnings.filterwarnings("ignore")

# setup the api
#genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Design the Page
st.title("Movie Recommendation System using Gemini-Pro")
user_input = st.text_input("Enter movie title, genre or keywords (e.g. Sci-FI Movie): ")

# Prompt Template
template = PromptTemplate(input_variables = ['user_input'],
                          template = '''Based on Preferences, here 
                          are the recommendations for {user_input}:\n''')

# Initialise the Model
llm = ChatGoogleGenerativeAI(model = "gemini-pro", api_key = os.getenv("GOOGLE_API_KEY"))

if user_input:
    prompt = template.format(user_input=user_input)
    recommendations = llm.predict(text = prompt)
    st.write(f'''Recommendations for You: \n{recommendations}''')
else:
    st.write("Please enter the Movie Preference")