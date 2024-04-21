import streamlit as st

def show():
    page_choice = st.selectbox("Select a location:", ["ABVMCRI Gate", "Russel Market"])
    if page_choice==''