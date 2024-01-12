
import csv



def read_vehicle_data():
    """Read vehicle data from a CSV file."""
    file_path = 'vehicles.csv'
    vehicles = []

    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicles.append(row)
    except FileNotFoundError:
        pass  

    return vehicles

def write_vehicle_data(vehicles):
    """Write vehicle data to a CSV file."""
    file_path = 'vehicles.csv'
    fieldnames = ['ID', 'Type', 'Model', 'RegistrationNumber']

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(vehicles)


# CRUD Functions
def add_vehicle():
    """Add a new vehicle to the system."""
    print("\nAdding a New Vehicle")
    vehicles = read_vehicle_data()

    vehicle_type = input("Enter vehicle type: ")
    model = input("Enter vehicle model: ")
    registration_number = input("Enter RegistrationNumber: ")

    last_id = 0 if not vehicles else int(vehicles[-1]['ID'])
    new_id = last_id + 1

    new_vehicle = {
        'ID': str(new_id),
        'Type': vehicle_type,
        'Model': model,
        'RegistrationNumber': registration_number
    }

    vehicles.append(new_vehicle)
    write_vehicle_data(vehicles)

    print("\nVehicle added successfully:")
    print(f"ID: {new_id}, Type: {vehicle_type}, Model: {model}, RegistrationNumber: {registration_number}")

def update_vehicle_by_id():
    """Update vehicle details by ID."""
    print("\nUpdating Vehicle by ID")
    vehicles = read_vehicle_data()

    vehicle_id = input("Enter vehicle ID to update: ")

    # Check if the vehicle exists
    vehicle_found = False
    for vehicle in vehicles:
        if vehicle['ID'] == vehicle_id:
            vehicle_found = True
            print(f"Vehicle with ID {vehicle_id} found.")
            print("Enter new details:")

            # Collect updated information (e.g., vehicle type, model, RegistrationNumber, etc.)
            vehicle_type = input("Enter updated vehicle type: ")
            model = input("Enter updated vehicle model: ")
            registration_number = input("Enter updated RegistrationNumber: ")

            # Update the vehicle details
            vehicle['Type'] = vehicle_type
            vehicle['Model'] = model
            vehicle['RegistrationNumber'] = registration_number

            write_vehicle_data(vehicles)
            print("\nVehicle updated successfully:")
            print(f"ID: {vehicle_id}, Type: {vehicle_type}, Model: {model}, RegistrationNumber: {registration_number}")
            break

    if not vehicle_found:
        print(f"No vehicle found with ID {vehicle_id}.")




    
def delete_vehicle_by_id():
    """Delete vehicle by ID."""
    print("\nDeleting Vehicle by ID")
    vehicles = read_vehicle_data()

    vehicle_id = input("Enter vehicle ID to delete: ")

    # Check if the vehicle exists
    vehicle_found = False
    for vehicle in vehicles:
        if vehicle['ID'] == vehicle_id:
            vehicle_found = True
            print(f"Vehicle with ID {vehicle_id} found and deleted.")
            vehicles.remove(vehicle)
            write_vehicle_data(vehicles)
            break

    if not vehicle_found:
        print(f"No vehicle found with ID {vehicle_id}.")

def view_vehicle_by_id():
    """View vehicle details by ID."""
    print("\nViewing Vehicle by ID")
    vehicles = read_vehicle_data()

    vehicle_id = input("Enter vehicle ID to view: ")

    # Check if the vehicle exists
    vehicle_found = False
    for vehicle in vehicles:
        if vehicle['ID'] == vehicle_id:
            vehicle_found = True
            print(f"Vehicle with ID {vehicle_id} details:")
            print(vehicle)
            break

    if not vehicle_found:
        print(f"No vehicle found with ID {vehicle_id}.")

def view_all_vehicles():
    """View details of all vehicles."""
    print("\nViewing All Vehicles")
    vehicles = read_vehicle_data()
   
    if vehicles:
        print("ID\tModel\tType\tRegistrationNumber")
        for vehicle in vehicles:
            print(f"{vehicle['ID']}\t{vehicle['Model']}\t{vehicle['Type']}\t{vehicle['RegistrationNumber']}")
    else:
        print("No vehicles found.")
# ...

def display_menu():
    """Display the menu options."""
    print("\nVehicle Management Menu:")
    print("1. Add Vehicle")
    print("2. Update Vehicle by ID")
    print("3. Delete Vehicle by ID")
    print("4. View Vehicle by ID")
    print("5. View All Vehicles")
    print("6. Exit")



def main_menu():
    """Main function for vehicle management."""
    print("Welcome to Vehicle Manager Portal")
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_vehicle()
        elif choice == '2':
            update_vehicle_by_id()
        elif choice == '3':
            delete_vehicle_by_id()
        elif choice == '4':
            view_vehicle_by_id()
        elif choice == '5':
            view_all_vehicles()
        elif choice == '6':
            print("Exiting the Vehicle Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    print("Exiting the Vehicle Management System.")

if __name__ == "__main__":
        main_menu()

        