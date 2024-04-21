# File: main.py
import streamlit as st
import homepage
import vr_tour
import audio_specs
import health_info

# Create a sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ('Homepage', 'VR Tour', 'Health Infographics','Audio Specifications'))

# Display the selected page content
if selected_page == 'Homepage':
    homepage.show()
elif selected_page == 'VR Tour':
    vr_tour.show()
elif selected_page == 'Audio Specifications':
    audio_specs.show()
elif selected_page == 'Health Infographics':
    health_info.show()

