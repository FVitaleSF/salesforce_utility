import streamlit as st
import requests

st.title("Choose Salesforce Item")

def call_api_service(api_service):
    endpoint = st.session_state.endpoint
    endpoint += api_service
    access_token = st.session_state.access_token
    headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": f"Bearer +{access_token}"
            }
    return {'endpoint':endpoint,'headers':headers}

def get_all_objects():

    api_service = '/services/data/v62.0/sobjects/'
    request_body = call_api_service(api_service)
    try:
        result = requests.get(request_body.get('endpoint'),headers=request_body.get('headers'))
        if result.status_code == 200:
            if 'objects' not in st.session_state:
                obj = result.json()
                obj_names = []
                for i in obj.get('sobjects'):
                    obj_names.append(i.get('name'))
                st.session_state.objects = obj_names

        else:
            raise ValueError('Something went wrong')
        
    except Exception as e:
        st.error(e)

try:
    get_all_objects()
except Exception as e:
    st.write(e)

selected_object = st.selectbox('Choose Object', options=st.session_state.objects)

def get_fields():

    try:
        api_service = f"/services/data/v62.0/sobjects/{selected_object}/describe"
        request_body = call_api_service(api_service)
        result = requests.get(request_body.get('endpoint'),headers=request_body.get('headers'))
        field_description = []
        for i in result.json().get('fields'):
            field_description.append(i.get('name'))
        return field_description
    except Exception as e:
        st.error(e)

if selected_object:
    selected_fields = st.multiselect('Choose Fields',options = get_fields())

st.number_input('Add Limit',min_value=1)


st.button('Go')


