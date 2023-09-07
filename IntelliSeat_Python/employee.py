import pandas as pd
import os

# Create a reservation DataFrame

def create_employee_dataframe():
    
    df_employee = pd.DataFrame()

    # Add columns to data frame
    df_employee['employee_firstname']= []
    df_employee['employee_lastname']= []
    df_employee['employee_id']= []
    df_employee['employee_friends']= []

    df_employee = pd.DataFrame(columns=["employee_firstname","employee_lastname", "employee_id", "employee_friends"], dtype=str)

    csv_file = 'employee_data.csv'

    # Check if the file already exists
    if os.path.isfile(csv_file):
        # File exists, do nothing
        print(f"The employee data frame already exists.")
        return
        
    else:
        # File does not exist, save the DataFrame
        df_employee.to_csv(csv_file, index=False)
        print(f"The DataFrame has been saved to '{csv_file}'.")


    # Save the dataframe
    df_employee = df_employee.to_csv('employee_data.csv', index=False)
    
    return df_employee

import os
import pandas as pd

def load_employee_dataframe():
    
    file_name='employee_data.csv'
    
    if os.path.isfile(file_name):
        df_employee = pd.read_csv(file_name)
        return df_employee
    else:
        print(f"The file '{file_name}' does not exist.")
        return None
    
def add_employee(employee_firstname, employee_lastname, employee_friends=""):

    df_employee = load_employee_dataframe()
    
    # Calculate the employee ID
    if 'employee_id' in df_employee.columns and not df_employee['employee_id'].empty:
        employee_id = df_employee['employee_id'].max() + 1
    else:
        employee_id = 1  # Start with 1 when there are no reservations
    
    new_row = {"employee_firstname" : employee_firstname, "employee_lastname" : employee_lastname, "employee_id" : employee_id, "employee_friends" : employee_friends}
    df_employee = df_employee.append(new_row, ignore_index=True)
    
    df_employee.to_csv('employee_data.csv', index=False)

    return df_employee

def get_employee_id(employee_firstname, employee_lastname):
    
    df_employee = load_employee_dataframe()
    
    # Check if an employee with the given name exists
    matching_employee = df_employee[(df_employee['employee_firstname'] == employee_firstname) & (df_employee['employee_lastname'] == employee_lastname)]
    
    if not matching_employee.empty:
        employee_id = matching_employee.iloc[0]['employee_id']
        print(f"Employee ID for {employee_firstname} {employee_lastname} is {employee_id}.")
        return
    else:
        print(f"No employee found with the name {employee_firstname} {employee_lastname}.")
        return
    
def remove_employee_by_id(employee_id):
    
    df_employee = load_employee_dataframe()
    
    # Search for employees with specific ID in employee data frame
    if employee_id in df_employee['employee_id'].values:
        
        df_employee = df_employee.drop(df_employee[df_employee['employee_id'] == employee_id].index)
        
        df_employee.to_csv('employee_data.csv', index=False)
        print(f"Employee with ID {employee_id} has been removed.")
        
    else:
        # Employee not found with ID
        print(f"No employee found with ID {employee_id}.")
    
    return df_employee

def get_all_employees():
    
    df_employee = load_employee_dataframe()
    
    # Get a list of all the employees
    employee_list = df_employee[['employee_firstname', 'employee_lastname', 'employee_id', 'employee_friends']].values.tolist()
    return employee_list

import pandas as pd

def add_friend(employee_id, friend_id):
    df_employee = load_employee_dataframe()

    # Check if the provided employee_id exists in the DataFrame
    if employee_id not in df_employee['employee_id'].values:
        print(f"Employee with ID {employee_id} not found.")
        return

    index_employee = df_employee[df_employee['employee_id'] == employee_id].index[0]
    current_friends = df_employee.at[index_employee, "employee_friends"]
    
    # Check if the employee is already friends with the provided friend_id
    if str(friend_id) in str(current_friends).split(','):
        print(f"Employee with ID {employee_id} is already friends with employee ID {friend_id}.")
        return

    # Update the employee's friends
    if pd.isna(current_friends) or current_friends == "":
        updated_friends = str(friend_id)
    else:
        updated_friends = f"{current_friends},{friend_id}"

    df_employee.at[index_employee, 'employee_friends'] = updated_friends

    # Save the updated DataFrame back to the CSV file
    df_employee.to_csv('employee_data.csv', index=False)

    print(f"Friend with ID {friend_id} added to employee with ID {employee_id}.")
    
def clear_all_employees():
    
    df_employees = load_employee_dataframe()
    
    # Drop all the reservations
    df_employees.drop(df_employees.index , inplace=True)
    
    df_employees.to_csv('employee_data.csv', index=False)
    
    return print("All employees have been deleted.")

def check_employee(firstname, lastname):
    
    df_employee = load_employee_dataframe()

    if not df_employee.empty:
        employee_exists = df_employee[(df_employee['employee_firstname'] == firstname) & (df_employee['employee_lastname'] == lastname)]
        return not employee_exists.empty
    else:
        return False  # Handle the case where the DataFrame couldn't be loaded
