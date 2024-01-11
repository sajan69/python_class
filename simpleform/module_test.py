from Modules.car import Car
from Modules.document import Document
from Modules.car_owner import CarOwner
from Modules.customer import Customer
from Modules.renting_process import RentingProcess


car = Car(name='Porsche', type='Carrera 4S', model='911', reg_no='PS911', owner='Sajan Adhikari', uploaded_on='2024-01-14', document='insurance.pdf')
customer = Customer(name='Aasish Ghising', address='Lakeside', phone_number='9824140179', email='aasish@gmail.com', license='EFGH5678')
car_document = Document(car, 'Insurance', 'insurance.pdf', '2024-01-11')
car_owner = CarOwner('Sajan Adhikari', '123 Main St', '123-456-7890', 'sajanac46@gmail.com', 'ABCD1234')
renting_process = RentingProcess(car, customer, '2024-01-15', '2022-01-17', 'Processing')

car.print_details()
car_document.print_details()
car_owner.print_details()
customer.print_details()
renting_process.print_details()
