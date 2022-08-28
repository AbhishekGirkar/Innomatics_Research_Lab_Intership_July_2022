import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Open Pub Locator",
    layout="wide")
    

st.markdown("<h1 style='text-align: center; color: red;'>Welcome To Open Pub Explorer</h1>", unsafe_allow_html=True)


Navbar= option_menu(
    menu_title=None,
    options=["Home"],
    icons=['None'],
    orientation="horizontal"
)


image= Image.open('Pub_image.jpg')

st.image(image, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("<h1 style='text-align: center; color: red;'>Open Pub Data</h1>", unsafe_allow_html=True)
df = pd.read_csv('C:/Users/Abhishek Girkar/Desktop/Streamlite/open_pubs_data.csv')
st.dataframe(df)

st.markdown("<h2 style='text-align: center; color: red;'>There is <I>50,563</I> active pubs in United Kingdom</h1>", unsafe_allow_html=True)
st.map(df)