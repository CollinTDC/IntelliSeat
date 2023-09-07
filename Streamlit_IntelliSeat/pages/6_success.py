#loading packages
import streamlit as st
import pages.reservation as reservation
import app

#header
st.header("See You in the Office!")
st.balloons()
#success message
st.success(f'Your successfully made a reservation for seat {app.seat_id} in {app.building_id} on {app.date}.')
    
import pandas as pd

df = pd.read_csv("reservation_data.csv")

# Convert date_str to datetime
if 'reservation_id' in df.columns and not df['reservation_id'].empty:
    reservation_id = df['reservation_id'].max() + 1
else:
    reservation_id = 1  # Start with 1 when there are no reservations

app.reservation_id = reservation_id

# Add the new reservation to the reservation dataframe
new_reservation = pd.DataFrame({
    "reservation_id": [reservation_id],
    "employee_id": [app.employee_id],
    "building_id": [app.building_id],
    "seat_id": [app.seat_id],
    "date": [app.date]
})

df = pd.concat([df, new_reservation], ignore_index=True)

date = app.date
building_id = app.building_id
employee_id = app.employee_id
firstname = app.firstname
lastname = app.lastname
reservation_id = app.reservation_id
seat_id = app.seat_id

app.date = ""
app.building_id = ""
app.employee_id = ""
app.firstname = ""
app.lastname = ""
app.reservation_id = ""
app.seat_id = ""

# Print and save the information
df.to_csv('reservation_data.csv', index=False)
#sharing the reservation with friends

share_with_friends = st.button("Share With Your Friends")
if share_with_friends:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import app

    # Email configuration
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP server port (usually 587 for TLS)
    smtp_username = 'collinarendsen@gmail.com'  # Replace with your email address
    # Replace with your email address
    smtp_password = 'vjnc evzg zqkz zdes'  # Replace with your email password

    invitation_text = (
        f"Hey Alberto Bacchelli,\n\n"
        f"Great news! Your colleague {firstname} {lastname} has reserved seat {seat_id} "
        f"in building {building_id} on {date}\n"
        "and wants you to be part of this exciting opportunity.\n\n"
        "Imagine the productive collaborations and connections waiting for you in this shared workspace.\n\n"
        f"{firstname} looks forward to seeing you there.\n\n"
        f"Use this link to reserve a seat: intelliseat.com/reservation.\n\n"
        "Best regards,\nYour IntelliSeat Team"
    )
    
    to_email = "thomas.hojsak@student.unisg.ch"
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = f"{firstname} {lastname} is going to be at the office!"
    msg.attach(MIMEText(invitation_text, 'plain'))

    # Establish a secure connection with the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(smtp_username, to_email, msg.as_string())
    server.quit()
    st.write("Your Friend Alberto has been invited.")

#switching to remove page
from streamlit_extras.switch_page_button import switch_page

#switching to another definition page
from streamlit_extras.switch_page_button import switch_page

continue_to_success = st.button("Logout")
if continue_to_success:
    switch_page("login")
