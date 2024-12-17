import requests
import streamlit as st
from urllib.parse import urljoin

class Salesforce_REST:

    def __init__(self,params):
        self.domain = params['domain']
        self.client_id = params["client_id"]
        self.client_secret = params["client_secret"]
        self.base_url = self.make_endpoint()
        self.access_token = self.authenticate()
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
    
    def make_endpoint(self):
        return f"https://{self.domain}.my.salesforce.com"

    def authenticate(self):
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",  # Set appropriate content type
            "Accept": "application/json",       # Optional, depending on API
        }

        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }

        try:
            
            auth_endpoint = f"{self.base_url}/services/oauth2/token"
            response = requests.post(auth_endpoint, data=body, headers=headers)
            response.raise_for_status()  
            access_token = response.json().get("access_token")

            if not access_token:
                raise ValueError("Access token not found in response")
            return access_token
        except requests.exceptions.RequestException as e:
            st.write(f"Error fetching token: {e}")
            return None

    def do_get(self,endpoint,query):
        
        full_endpoint = full_endpoint = urljoin(self.base_url, endpoint)

        try:
            params = {'q': query}
            result = requests.get(full_endpoint,
                        headers=self.headers,
                        params=params)
            return result.json()

            st.write(classes)
        except Exception as e:
            st.error(e)    

    def do_post(self):
        return True
    

