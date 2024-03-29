import csv
import getpass

def check_email_exists(email):
    '''
    Checks whether the registerd email already exist in the database!!
    
    '''
    file_path = 'accounts.csv'
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Email'] == email:
                return True
    return False


def validate_email(email):
    
    '''
    Validate email: @, .com required
    '''
    if '@' in email and email.endswith('.com'):
        return True
    return False

def register(email):

    if not validate_email(email):
        print("Invalid email format. Email must contain '@' and end with '.com'.")
        return

    if check_email_exists(email):
        print("An account with this email already exists.")
        return

    username = input("Enter your username: ").strip()

    while True:
        password = getpass.getpass("Enter your password: ").strip()
        confirm_password = getpass.getpass("Confirm your password: ").strip()

        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            break

    file_path = 'accounts.csv'

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Email', 'Username', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Email': email, 'Username': username, 'Password': password})
    print("Account created successfully!")

if __name__ == "__main__":
    register()
