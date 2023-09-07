#loading packages
import streamlit as st
import datetime
import app

#header

st.header("IntelliSeat", divider="red")
st.subheader("Plan Ahead: Choose a Date")

#date -> calander
d = st.date_input("Please use the calendar to select your preferred date:")

app.date = str(d)


#switching to next page
from streamlit_extras.switch_page_button import switch_page

continue_to_spaces = st.button("Check Space Availability")
if continue_to_spaces:
    switch_page("spaces")