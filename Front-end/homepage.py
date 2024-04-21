# File: homepage.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import pandas as pd
import pydeck as pdk
from PIL import Image

st.set_page_config(page_title = "DhyanaVR", page_icon = ":unicorn:", layout = "wide")
def get(path:str):
    with open(path, "r") as f:
        return json.load(f)
    animation_data = f.read()
path = get("./meditation.json")

def show():

    with st.container():
        st.title("Welcome to DhyanaVR 🧘")
        st.subheader("Conceptualization 💡")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write("The inner ear's compass spins haywire, plunging us into a dizzying world.  Meanwhile, the elusive peace of meditation remains just out of reach, lost in the daily chaos.  Can a fantastical portal, crafted from VR, become a training ground for the wayward balance system and a haven for the restless mind? ")
            st.write("[More Information about the Project >](https://www.canva.com/design/DAGC4YS7vm8/ekBtb1hNoaM3r-oZldobXQ/edit?utm_content=DAGC4YS7vm8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)")
            img_contact_form = Image.open("./dhyanavr.jpg")
            st.image(img_contact_form, width=250, channels = "RGB")

        with right_column:
     
            st_lottie(path, height=500, width=400)

        st.title("VR Headset in view")

        iframe_code = """
       <iframe width="100%" height="400" src="https://sketchfab.com/models/51b8dbff65e247979f068914f6197909/embed" frameborder="0" allow="autoplay; fullscreen; mixer; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
     """

        st.markdown(iframe_code, unsafe_allow_html=True)

            