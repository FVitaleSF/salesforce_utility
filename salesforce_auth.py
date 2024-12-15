import requests
import streamlit as st

class salesforce_auth:

    def __init__(self, sf_domain, client_id, secret):
        self._sf_domain = sf_domain  
        self._client_id = client_id
        self._secret = secret

    def authorize_service(self):
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",  # Set appropriate content type
            "Accept": "application/json",       # Optional, depending on API
        }

        body = {
            "client_id": self._client_id,
            "client_secret": self._secret,
            "grant_type": "client_credentials"
        }

        end_point = f"https://{self._sf_domain}.my.salesforce.com/services/oauth2/token"
        try:

            response = requests.post(end_point, data=body, headers=headers)
            response.raise_for_status()  
            access_token = response.json().get("access_token")

            if not access_token:
                raise ValueError("Access token not found in response")
            return access_token
        except requests.exceptions.RequestException as e:
            st.write(f"Error fetching token: {e}")
            return None
