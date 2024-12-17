import streamlit as st

class tooling_api:

    def api_service():
        endpoint = st.session_state.endpoint
        endpoint += api_service
        access_token = st.session_state.access_token
        headers = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer +{access_token}"
                }
        return {'endpoint':endpoint,'headers':headers}

    def class_query():
        query = "SELECT Id, Name FROM ApexClass"
        params = {'q': query}
        return True
    


