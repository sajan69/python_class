class CarOwner:
    def __init__(self, name, address, phone_number, email, license):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.license = license

    def print_details(self):
        print(f"""
               Owner Details
            Name: {self.name}
            Address: {self.address}
            Phone Number: {self.phone_number}
            Email: {self.email}
            License: {self.license}
        """)

    def save_to_file(self):
        # Implement saving car owner details to a file
        pass
