import streamlit as st
from Salesforce_REST import Salesforce_REST

params = {}

params['domain'] = st.text_input('Add endpoint',placeholder="your_domain")
params["client_id"] = st.text_input('Add Client Id')
params["client_secret"] = st.text_input('Add Client Secret')

def authenticate():
    if not params['domain'] or not params["client_id"] or not params["client_secret"]:
        st.error("All fields are required!")
        return
    try:
        api_service = Salesforce_REST(params)
        st.session_state.salesforce_api = api_service
        st.session_state.access_token = api_service.access_token     
        st.session_state.authenticated = True
        st.success('You succesfully logged in!')

        if 'base_url' not in st.session_state:
            st.session_state.endpoint = api_service.base_url

    except Exception as e:
        st.session_state.authenticated = False
        st.error(f"An error occurred {e}")

st.button('Authorize',on_click=authenticate())