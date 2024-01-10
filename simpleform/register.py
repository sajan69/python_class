import csv

def register():
    email = input("Enter your email: ").strip()
    username = input("Enter your username: ").strip()
    return email, username

def save_account(email, username, password):
    file_path = 'accounts.csv'

    file_exists = check_file_exists(file_path)

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Email', 'Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Email': email, 'Username': username, 'Password': password})
    print("Account created successfully!")

def check_file_exists(file_path):
    try:
        with open(file_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False
