import pandas as pd
import os

# Create a reservation DataFrame

def create_reservation_dataframe():
    df = pd.DataFrame()

    # Add columns to data frame
    df['reservation_id'] = []
    df['employee_id'] = []
    df['building_id'] = []
    df['date'] = []
    df['seat_id'] = []
    
    # Convert columns to correct types
    df = pd.DataFrame(columns=["reservation_id", "employee_id", "building_id", "seat_id", "date"], dtype=object)
    df['date'] = pd.to_datetime(df['date'])

    csv_file = 'reservation_data.csv'

    # Check if the file already exists
    if os.path.isfile(csv_file):
        # File exists, do nothing
        print(f"The reservation data frame already exists.")
        return
        
    else:
        # File does not exist, save the DataFrame
        df_reservations = df.to_csv('reservation_data.csv', index=False)
        print(f"The DataFrame has been saved to '{csv_file}'.")


    # Save the dataframe
    
    return df_reservations

import os
import pandas as pd

def load_reservation_dataframe():
    
    file_name='reservation_data.csv'
    
    if os.path.isfile(file_name):
        df_reservations = pd.read_csv(file_name)
        return df_reservations
    else:
        print(f"The file '{file_name}' does not exist.")
        return None
    
# Create new reservation entry

from datetime import datetime

def add_reservation(employee_id, building_id, seat_id, date_str):
    
    df = load_reservation_dataframe()
    
    # Convert date_str to datetime
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # When the desk in the building is already reserved on that date
    if not df[(df['building_id'] == building_id) & (df['seat_id'] == seat_id) & (df['date'] == date_str)].empty:
        return f"Desk {seat_id} in building {building_id} is already reserved for {date_str}."
    
    # Calculate the reservation ID
    if 'reservation_id' in df.columns and not df['reservation_id'].empty:
        reservation_id = df['reservation_id'].max() + 1
    else:
        reservation_id = 1  # Start with 1 when there are no reservations

    # Add the new reservation to the reservation dataframe
    new_reservation = {"reservation_id": reservation_id, "employee_id": employee_id, "building_id": building_id, "seat_id": seat_id, "date": date_str}
    df = df.append(new_reservation, ignore_index=True)
    
    # Print and save the information
    df.to_csv('reservation_data.csv', index=False)

    return f"Desk {seat_id} in building {building_id} is successfully reserved for {date_str}."

## TODO: check if building exists, check if seat exists!!

def remove_reservation(reservation_id):

    
    df_reservations = load_reservation_dataframe()
        
    is_id_in_dataframe = reservation_id in df_reservations['reservation_id'].values
    
    df_reservations = df_reservations.drop(df_reservations[df_reservations['reservation_id'] == reservation_id].index)
    df_reservations.to_csv('reservation_data.csv', index=False)
    
    if is_id_in_dataframe:
        return "The reservation with the ID: " + str(reservation_id) + " has been removed."
    else:
        return "The entered ID: " + str(reservation_id) + " has not been been found."
    
def get_reserved_seats():
    
    # Load data frame with reservations
    df_reservations = load_reservation_dataframe()
    
    # Get all the reserved seats
    reserved_seats = df_reservations["seat_id"]

    return reserved_seats.tolist()

import pandas as pd
from datetime import datetime

def get_seats_in_building(building_id, date_str):
    
    # Load data frame with seats
    df_seats = pd.read_csv('seat_data.csv')
    
    # Filter all seats in the specified building
    seats_in_building = df_seats[(df_seats['building_id'] == building_id)]

    
    if not seats_in_building.empty:
        
        # Create list with seats in specified building
        seat_in_building_list = []
        seat_in_building_list.append(seats_in_building["seat_id"])
        seat_in_building_list = seats_in_building['seat_id'].tolist()
            
        return seat_in_building_list
    else:
        print(f"No seats found in Building {building_id} on {date}.")
        return None
    
def get_free_seats_in_building_on_day(building_id, date_str):
            
    df_reservations = load_reservation_dataframe()
    
    # Get all the reserved seats
    all_reserved_seats = get_reserved_seats()
    
    # Get all the seats in the building
    seats_in_building = get_seats_in_building(building_id)
    
    # Create two lists to add the seats
    reserved_seats_building = []
    free_seats = []
    
    # Get all reserved seats in the specified building
    reserved_seats_for_date = []
    
    # Check if there are any reservations for the seat on the specified date
    for seat in seats_in_building:
        reservations_for_seat_on_date = df_reservations[(df_reservations['seat_id'] == seat) & (df_reservations['date'] == date_str)]
        
        if seat not in all_reserved_seats or reservations_for_seat_on_date.empty:
            free_seats.append(seat)
        else:
            reserved_seats_for_date.append(seat)

    free_seats_sorted = sorted(free_seats)
    
    return free_seats_sorted

def get_amount_of_free_seats(building_id, date_str):
    
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    empty_seats = get_free_seats_in_building_on_day_1(building_id, date_str)

    return f"{len(empty_seats)} seats left in building {building_id} on {date}."

def clear_all_reservations():
    
    df_reservations = load_reservation_dataframe()
    
    # Drop all the reservations
    df_reservations.drop(df_reservations.index , inplace=True)
    
    df_reservations.to_csv('reservation_data.csv', index=False)
    
    return print("All reservations have been deleted.")

from datetime import datetime
import pandas as pd

# Remove all the reservations in the past. Run this daily to clear the reservation data frame
def update_reservation_list():
    
    df_reservations = load_reservation_dataframe()
    current_date = pd.to_datetime(datetime.now().date())

    # Convert the 'date' column in the DataFrame to datetime objects
    df_reservations['date'] = pd.to_datetime(df_reservations['date'])

    # Check whether date in the past
    df_reservations = df_reservations[df_reservations['date'] >= current_date]
    
    # Save the updated DataFrame to the CSV file
    df_reservations.to_csv('reservation_data.csv', index=False)

    return print(f"The reservation list has been updated. All reservations in the past have been removed.")

def get_reservations_by_employee(employee_id):
    
    df = load_reservation_dataframe()

    employee_reservations = df[df['employee_id'] == employee_id]
    
    return employee_reservations
