# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Google API key for Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to fetch response from Gemini API
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Set up Streamlit page configuration and title
st.set_page_config(page_title="Q&A Chatbot Demo", layout='wide')

# Streamlit header and main content area
st.title("Gemini Q&A Chatbot")

# Input field for user to enter their question
input_question = st.text_input("Enter your question:")

# Button to submit the question
if st.button("Ask"):
    if input_question:
        # Fetch response from Gemini API based on user's question
        response_text = get_gemini_response(input_question)
        # Display the response in a formatted way
        st.subheader("Response:")
        st.markdown(f"> {response_text}")
    else:
        st.warning("Please enter a question.")

# Footer section with additional information or links
st.sidebar.title("About")
st.sidebar.info(
    "This Q&A Chatbot is powered by the Gemini API from Google GenerativeAI. "
    "Ask questions and get responses based on the Gemini model."
    "\n\n"
    "Developed by Lavish Gangwani"
)

