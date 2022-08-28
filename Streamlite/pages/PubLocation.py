import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Pub Location",
    layout="wide"
)

Navbar= option_menu(
    menu_title=None,
    options=["Pub Location"],
    icons=['None'],
    orientation="horizontal"
)


df = pd.read_csv('open_pubs_data.csv')
st.markdown("<h3 style='text-align: center; color: Blue;'>Local Authority Name</h3>", unsafe_allow_html=True)
title = st.text_input('Local Authority Name', 'Mid Suffolk')
st.markdown(title)

fetching_local_data = df.loc[df.local_authority == title,['latitude','longitude']]
st.map(fetching_local_data)

fetching_local_name = df.loc[df.local_authority == title,['name','address']].reset_index(drop=True)
st.markdown('Area Name"s and Address')
st.dataframe(fetching_local_name)