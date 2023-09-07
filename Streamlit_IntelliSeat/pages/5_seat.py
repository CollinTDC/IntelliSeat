#loading packages
import streamlit as st
import pages.reservation as reservation
import app
import numpy as np
import pages.seat as seat

building_id = str(app.building_id)
date_str = str(app.date)


seat_list = reservation.get_free_seats_in_building_on_day(building_id, date_str)
seat_list_array = np.array(seat_list)

result = ["Seat " + str(num) for num in seat_list_array]


#select seat type
st.header("IntelliSeat", divider="red")
st.subheader("Select Your Favorite Seat.")
text = (f"The following seats are still available on {app.date} in {building_id}.")
types = []

import pandas as pd 

df_seats = pd.read_csv("seat_data.csv")

for x in seat_list:
    seat_type = df_seats.loc[df_seats["seat_id"] == x, "seat_type"].values[0]
    types.append(seat_type)

types_array = np.array(types)

#select indivual seat 

selection = st.radio(
    text,
    result,
    captions=types_array)


seat_str = selection.split()[-1]
app.seat_id = seat_str


#switching to next page
from streamlit_extras.switch_page_button import switch_page

continue_to_success = st.button("Complete Reservation")
if continue_to_success:
    switch_page("success")
    app.add = True

    