import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Nearest Pub",
    layout="wide"
)

df = pd.read_csv('open_pubs_data.csv')

Navbar= option_menu(
    menu_title=None,
    options=["Nearest Pubs"],
    icons=['None'],
    orientation="horizontal"
)

st.markdown("<h3 style='text-align: center; color: Blue;'>Find Nearest Pub from current Location</h3>", unsafe_allow_html=True)




lat = st.number_input('Latitude')
lon = st.number_input('Longitude')
button = st.button("Find")
df_new = df[['latitude', 'longitude']]
new_points = np.array([lat, lon])

# Calculate distance between new_points and all points in df_new using Euclidean distance 
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))


# sort the array using arg partition and keep only 5 elements
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.text("The location corresponding to below minimum distances : ")
    st.dataframe(df.iloc[min_indices])
    st.map(df.iloc[min_indices])