import getpass
from register import register, save_account
from login import login, check_credentials

def main():
    while True:
        print("\nWelcome!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email, username = register()
            password = getpass.getpass("Enter your password: ").strip()
            save_account(email, username, password)
        elif choice == '2':
            username, password = login()
            password = getpass.getpass("Enter your password: ").strip()
            check_credentials(username, password)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
