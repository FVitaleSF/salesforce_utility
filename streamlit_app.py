import streamlit as st

DEFAULT_PAGE = [st.Page('pages/login.py',title='Login')]
AUTH_PAGES = [st.Page('pages/records_get.py',title='Build Reports'),st.Page('pages/add_records.py',title='Add Entries')]


def logout():
    st.session_state.access_token = None
    st.session_state.authenticated = False

if 'display_pages' not in st.session_state:
    display_pages = DEFAULT_PAGE.copy()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'access_token' not in st.session_state:
    st.session_state.access_token = None

if st.session_state.authenticated:
    display_pages = AUTH_PAGES.copy()
    st.sidebar.button('Logout',on_click=logout)


pg = st.navigation(display_pages,position="sidebar")
pg.run()