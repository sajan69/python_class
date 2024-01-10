import getpass
from register import register, check_email_exists
from login import login

def main():
    while True:
        print("\nWelcome!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter your email: ").strip()
            if not check_email_exists(email):
                register()
            else:
                print("An account with this email already exists.")
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
