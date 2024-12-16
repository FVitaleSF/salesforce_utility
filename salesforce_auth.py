import requests
import streamlit as st

class salesforce_auth:

    def __init__(self, sf_domain, client_id, secret):
        self._sf_domain = sf_domain
        self._client_id = client_id
        self._secret = secret
        self.endpoint = self.make_endpoint() 
    
    def make_endpoint(self):

        return f"https://{self._sf_domain}.my.salesforce.com"



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

        try:
            
            auth_endpoint = f"{self.endpoint}/services/oauth2/token"
            response = requests.post(auth_endpoint, data=body, headers=headers)
            response.raise_for_status()  
            access_token = response.json().get("access_token")

            if not access_token:
                raise ValueError("Access token not found in response")
            return access_token
        except requests.exceptions.RequestException as e:
            st.write(f"Error fetching token: {e}")
            return None
