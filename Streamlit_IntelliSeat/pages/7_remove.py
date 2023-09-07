#loading packages
import streamlit as st


#remove reservation
#header
st.header("Mistakes happen - cancel your reservation")

#add reservation

#switching to next page
from streamlit_extras.switch_page_button import switch_page

continue_to_login = st.button("Make another reservation")
if continue_to_login:
    switch_page("building")