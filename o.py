# from dotenv import load_dotenv
# load_dotenv()  # Make sure to call load_dotenv to actually load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the API key (consider moving it to an environment variable for security)
genai.configure(api_key="AIzaSyBXmSE8mWln6RxJG7LHO1WLb1ThA9HJNwg")

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")
st.header("Q&A LLM Application")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Input:", key="user_input")
submit = st.button("Ask the Question")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.session_state['chat_history'].append(("User", user_input))
    
    # Display the response
    st.subheader("RESPONSE FROM MODEL:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Assistant", chunk.text))

# Display chat history
st.subheader("HISTORY")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
