import csv

def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    return username, password

def check_credentials(username, password):
    file_path = 'accounts.csv'

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Username'].strip() == username and row['Password'].strip() == password:
                print("Login successful!")
                return True
        print("Invalid username or password.")
        return False
