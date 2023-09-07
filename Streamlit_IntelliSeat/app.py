
#loading packages
import streamlit as st
import datetime
import json
import requests
import pandas as pd
import numpy as np

from streamlit_lottie import st_lottie

firstname = ""
lastname = ""
employee_id = ""
building_id = ""
date = ""
space_left = 0
seat_id = 0
admin = False
add = False
reservation_id = ""



#configurate page
st.set_page_config(page_title = "Homepage", layout="wide")



#Title
st.title("IntelliSeat")
st.header("", divider="red")


#Adding a a subheader
st.subheader("Say goodbye to office chair roulette and hello to hassle-free workspace reservations!")
st.subheader("Introducing IntelliSeat, where finding and booking the perfect desk is as easy as a few taps. Revolutionize your workday experience today!")


#adding an animation 

url = requests.get(
    "https://lottie.host/8cc20c70-cdf4-43d3-8bfe-217e3c228906/K4FmmsLueH.json")
url_json = dict()

if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in the URL")
        

st_lottie(url_json,
        # height and width of animation
        height=200,  
        width=200,
        # speed of animation
        speed=1,  
        # means the animation will run forever like a gif, and not as a still image
        loop=True,  
        # quality of elements used in the animation, other values are "low" and "medium"
        quality='high',
        # THis is just to uniquely identify the animation
        key='Office' 
        )

#Switching to the next page (login page) with an interactive button
from streamlit_extras.switch_page_button import switch_page
continue_to_login = st.button("Reserve a Seat")
if continue_to_login:
        switch_page("login")












