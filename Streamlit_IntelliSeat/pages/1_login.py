#loading packages
import streamlit as st
import pages.employee as employee 
import pandas as pd
import app

#header and lead
st.header("IntelliSeat", divider="red")
st.subheader("Welcome Back!")
st.caption("Log in to continue:")


#first name, last name password 
#switching to next page

with st.form(key='my_form'):
    firstname = st.text_input('Enter your first name:')
    lastname = st.text_input("Enter your last name:")
    app.firstname = firstname
    app.lastname = lastname
    login = st.form_submit_button('Login')

    if login:

        if firstname == "Admin" and lastname == "Admin":
            print("hello")

        check_employee = employee.check_employee(firstname, lastname)

        if check_employee == True:


            df_employee = pd.read_csv("employee_data.csv")
            
            # Check if an employee with the given name exists
            matching_employee = df_employee[(df_employee['employee_firstname'] == firstname) & (df_employee['employee_lastname'] == lastname)]
            employee_id = matching_employee.iloc[0]['employee_id']
            app.employee_id = employee_id

            print("hello")

        else:
            st.text("Please enter a valid first and last name.")
