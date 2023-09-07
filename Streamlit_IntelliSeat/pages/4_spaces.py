import streamlit as st
import app
import pages.reservation as reservation

#how many spaces are left
st.header("IntelliSeat", divider="red")
st.subheader("Space Availability")

building_id = str(app.building_id)
date_str = str(app.date)

st.write(reservation.get_amount_of_free_seats(building_id, date_str))


#switching to next page
from streamlit_extras.switch_page_button import switch_page

continue_to_seat = st.button("Choose Seat")
if continue_to_seat:
    switch_page("seat")
    