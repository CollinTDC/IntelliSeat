#loading packages
import streamlit as st
import app 
import pages.seat as seat
import numpy as np
import pages.employee as employee
import pandas as pd

#header

firstname = app.firstname
lastname = app.lastname

st.header("IntelliSeat", divider="red")
st.title(f"Hi {firstname}, Your Next Office Visit Awaits.")
st.divider()

df_reservations = pd.read_csv("reservation_data.csv")

reservations = df_reservations[df_reservations["employee_id"] == app.employee_id]

if not reservations.empty:
    st.subheader("You Have the Following Reservations:")
    for index, row in reservations.iterrows():
        building_id = row["building_id"]
        seat_id = row["seat_id"]
        date = row["date"]
        st.write(f"Seat {int(seat_id)} in {building_id} on {date}")


else:
    st.write("You haven't made any reservations.")

st.divider()

st.subheader("Reserve a Seat")

data_list = ["theSTUDY", "theMEET", "theWORK"]
data_array = np.array(data_list)

option = st. selectbox("Please select your preferred office building:", data_array)
app.building_id = option

#switching to next page
from streamlit_extras.switch_page_button import switch_page

continue_to_date = st.button("Continue")
if continue_to_date:
    switch_page("date")