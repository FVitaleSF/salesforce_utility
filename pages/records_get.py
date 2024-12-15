import streamlit as st
import requests

st.title("Welcome to the Home Page!")

# Access the stored access token
if 'access_token' in st.session_state:
    st.write(f"Access Token: {st.session_state.access_token}")
else:
    st.error("You are not authenticated. Please go back to the main page.")
