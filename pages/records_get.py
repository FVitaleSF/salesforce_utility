import streamlit as st
import requests
from fields_describe import fields_describe

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
        return result.json().get('fields')
        
    except Exception as e:
        st.error(e)

def get_field_names(fields):
    return fields_describe.get_field_names(fields)

def get_fields_properties(fields):
    return True

st.session_state.object_fields = get_fields()

if selected_object:
    selected_fields = st.multiselect('Fields to Display',options = get_field_names(st.session_state.object_fields))

st.number_input('Add Limit',min_value=1)

st.write(fields_describe.get_fields_properties(st.session_state.object_fields))

@st.dialog('Filters')
def add_filters():
    st.write(get_field_names(st.session_state.object_fields))

if st.button('Add Filters'):
    add_filters()




