import streamlit as st
import matplotlib.pyplot as plt

import mymodule

arr = mymodule.make_data()

fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

with st.sidebar:
    st.markdown(
        "<p style='text-align: center; color: grey;'><a href='https://www.kitware.com/' target='_blank'><img src='https://img.shields.io/badge/Made%20by-Kitware-blue' alt='Made by Kitware'> </a></p>",
        unsafe_allow_html=True,
    )
