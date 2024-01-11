class RentingProcess:
    def __init__(self, car, customer, rent_start_date, rent_end_date, payment_status):
        self.car = car
        self.customer = customer
        self.rent_start_date = rent_start_date
        self.rent_end_date = rent_end_date
        self.payment_status = payment_status

    def print_details(self):
        print(f"""
               Renting Process
            Car: {self.car.name} ({self.car.reg_no})
            Customer: {self.customer.name}
            Rent Period: {self.rent_start_date} to {self.rent_end_date}
            Payment Status: {self.payment_status}
        """)

    def save_to_file(self):
        # Implement saving renting process details to a file
        pass
