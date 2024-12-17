import streamlit as st
from Salesforce_REST import Salesforce_REST

if 'salesforce_api' in st.session_state:
    sf_api = st.session_state.salesforce_api
else:
    st.rerun(scope="app")

def get_classes():
    query = "SELECT Name,Id FROM ApexClass WHERE NOT (Name LIKE '%test%')"
    endpoint = '/services/data/v62.0/tooling/query'
    
    try:
        return sf_api.do_get(endpoint,query)
    except Exception as e:
        st.error(f"Error fetching Apex classes: {e}")

def get_class_names():
    parsed_result = get_classes()
    classes = {}
    for i in parsed_result['records']:
        classes[(i['Name'])] = i['Id']
    st.session_state.apex_classes = classes
    return classes



if 'apex_classes' not in st.session_state:
    apex_classes = get_class_names()
        
selected_classes = st.multiselect('Choose classes',options = st.session_state.apex_classes)

def get_test_classes():
    st.write(selected_classes)
    
if selected_classes:
    get_test_classes()
    