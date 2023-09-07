import employee as employee 
import reservation as reservation
import seat as seat

# Create dataframes
employee.create_employee_dataframe()
reservation.create_reservation_dataframe()
seat.create_seats_dataframe()
seat.create_buildings_file()

employee.add_employee("Collin", "Arendsen")
employee.add_employee("Noemi", "Abed")
employee.add_employee("Thomas", "Hojsak")
employee.add_employee("Charlotte", "Blanc")






