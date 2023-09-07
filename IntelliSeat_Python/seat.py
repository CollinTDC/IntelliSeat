import pandas as pd
import os

# create a seats DataFrame

def create_seats_dataframe():
    df_seats=pd.DataFrame()
        
    #Add columns to data frame
    df_seats['building_id']=[]
    df_seats['seat_id']=[]
    df_seats['seat_type']=[]
    
    df_seats = pd.DataFrame(columns=["building_id", "seat_id","seat_type"], dtype=str)
    df_seats = df_seats.to_csv('seat_data.csv', index=False)

    # Create a DataFrame with two columns "building_id" and "seat_id" both of dtype int
    
    csv_file = 'seat_data.csv'
                                   
    # Check if the file already exists
    if os.path.isfile(csv_file):
        # File exists, do nothing
        print(f"The seat data frame already exists.")
        return
        
    else:
        # File does not exist, save the DataFrame
        df_seats.to_csv(csv_file, index=False)
        print(f"The DataFrame has been saved to '{csv_file}'.")
                                   
      
    # Save the dataframe
    df_seats = df_seats.to_csv('seat_data.csv', index=False)
    
    return df_seats

import os
import pandas as pd

def load_seat_dataframe():
    
    file_name='seat_data.csv'
    
    if os.path.isfile(file_name):
        df_seat = pd.read_csv(file_name)
        return df_seat
    else:
        print(f"The file '{file_name}' does not exist.")
        return None
    
    
def check_building(building_id):
    try:
        with open("buildings_list.txt", 'r') as file:
            for x in file:
                if building_id in x:
                    return True
    except FileNotFoundError:
        return False
    return False

def add_seat(building_id, seat_type):

    df_seats = load_seat_dataframe()
    
    # Calculate the seat ID
    if 'seat_id' in df_seats.columns and not df_seats['seat_id'].empty:
        seat_id = df_seats['seat_id'].max() + 1
    else:
        seat_id = 1  # Start with 1 when there are no reservations
        
    if not check_building(building_id):
        print(f"The building '{building_id}' does not exist.")
        return
        
    new_row = {"building_id" : building_id, "seat_id" : seat_id, "seat_type" : seat_type}
    df_seats = df_seats.append(new_row, ignore_index=True)
    
    df_seats.to_csv('seat_data.csv', index=False)
    print(f"A seat with ID {seat_id} has been added to the building {building_id}.")

    return

def remove_seat_by_id(seat_id):
    
    df_seats = load_seat_dataframe()
    
    # Search for seats with specific ID in seat data frame
    if seat_id in df_seats['seat_id'].values:
        
        df_seats = df_seats.drop(df_seats[df_seats['seat_id'] == seat_id].index)
        
        df_seats.to_csv('seat_data.csv', index=False)
        print(f"Seat with ID {seat_id} has been removed.")
        
    else:
        # Seat not found with ID
        print(f"No seat found with ID {seat_id}.")
    
    return df_seats

def get_all_seats():
    
    df_seats = load_seat_dataframe()
    
    # Get a list of all the seats
    seats_list = df_seats[['building_id', 'seat_id', 'seat_type']].values.tolist()
    return seats_list

def create_buildings_file():
    
    starting_buildings_list = ["theSTUDY", "theMEET", "theWORK"]
 
    with open("buildings_list.txt", "w") as file:
        for x in starting_buildings_list:
            file.write(x + "\n")
            
    return print("New buildings list created or reset.")

def add_building(name):
    
    # Check if the building name already exists in the file
    with open("buildings_list.txt", "r") as file:
        existing_buildings = file.read().splitlines()
        
        if name in existing_buildings:
            print(f"{name} already exists in the list of buildings.")
            return

    # If the name doesn't exist, append it to the file
    with open("buildings_list.txt", "a") as file:
        file.write(name + '\n')

    print(f"{name} has been added.")
    
def get_all_buildings():

    with open("buildings_list.txt", "r") as file:
        buildings = file.read().splitlines()
    return buildings
