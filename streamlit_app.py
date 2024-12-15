import streamlit as st
from salesforce_auth import salesforce_auth


st.title('Authorize to Salesforce')

endpoint = st.text_input('Add endpoint',placeholder="your_domain")
client_id = st.text_input('Add Client Id')
client_secret = st.text_input('Add Client Secret')

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'access_token' not in st.session_state:
    st.session_state.access_token = None

def authenticate():
    if not endpoint or not client_id or not client_secret:
        st.error("All fields are required!")
        return
    try:
        params = salesforce_auth(endpoint,client_id,client_secret)
        st.session_state.access_token = params.authorize_service()      
        st.session_state.authenticated = True

    except Exception as e:
        st.session_state.authenticated = False
        st.error(f"An error occurred {e}")

st.button('Authorize',on_click=authenticate)

if 'authenticated' in st.session_state:
    st.navigation([st.Page('records_get.py')])