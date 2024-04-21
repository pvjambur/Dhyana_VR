import streamlit as st
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

# Define a function to create a fitness measurement dashboard
def show():
    st.title('Virtual Reality Meditation Environment')

    
    page_choice = st.selectbox("Select a location for the VR Visuals:", ["Amidst trees and mountains", "A virtual Golden Gate Bridge", "Amidst the mighty Himalayas"])
    
    if page_choice=="Amidst trees and mountains":
        st.subheader("Amidst trees and mountains")
        st.write("Amidst the verdant embrace of towering trees and the majestic rise of undulating mountains, there lies a realm where the whispers of nature are more articulate than any human speech. Here, the air is perfumed with the earthy scent of pine and the freshness of unseen blossoms, mingling together in a symphony of fragrances that beckons the soul to wander and wonder.")
        iframe_code = """
       <iframe width="100%" height="400" src="https://sketchfab.com/models/a78ae6a11957401a83fd074004aafcc0/embed" frameborder="0" allow="autoplay; fullscreen; mixer; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
     """

        st.markdown(iframe_code, unsafe_allow_html=True)

    if page_choice=="A virtual Golden Gate Bridge":
        st.subheader("A virtual Golden Gate Bridge")
        st.write("The Golden Gate Bridge, a marvel of modern engineering, stretches across the churning waters of the San Francisco Bay, its iconic orange spires piercing the fog like beacons of the West Coast. Below, the river, a vital artery of commerce and nature, mirrors the sky as it meanders past cityscapes and under the bridge’s grand arches. Together, they create a postcard-perfect tableau that symbolizes both human ambition and the serene majesty of the natural world.")
        iframe_code = """
       <iframe width="100%" height="400" src="https://sketchfab.com/models/6fab41b2c10740cfa3286410d5dbaea3/embed" frameborder="0" allow="autoplay; fullscreen; mixer; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
     """

        st.markdown(iframe_code, unsafe_allow_html=True)

    if page_choice=="Amidst the mighty Himalayas":
        st.subheader("Amidst the mighty Himalayas")
        st.write("The Himalayas stand as a testament to nature's grandeur, where the sky is painted with the delicate hues of dawn, casting a golden glow over the snow-laden peaks. In the silence of these towering giants, one can hear the soft whispers of ancient glaciers and the distant rumble of avalanches, like the earth's own heartbeat. Here, in the embrace of these eternal sentinels, time seems to pause, allowing the soul to soar on the wings of the crisp, mountain air.")
        iframe_code = """
       <iframe width="100%" height="400" src="https://sketchfab.com/models/e086183da4854416a606dc4f3bbea3ae/embed" frameborder="0" allow="autoplay; fullscreen; mixer; vr" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
     """

        st.markdown(iframe_code, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")







    
   