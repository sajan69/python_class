
class Car:
    def __init__(self,name, type, model, reg_no, owner, uploaded_on, document ):
        self.name = name
        self.type = type
        self.model = model
        self.reg_no = reg_no
        self.owner = owner
        self.uploaded_on = uploaded_on
        self.document = document

    def print_details(self):
        print(f"""
            Name: {self.name}
            Type: {self.type}
            Model: {self.model}
            Owner: {self.owner}
            Registration Number: {self.reg_no}
            Owner: {self.owner}
            Uploaded On: {self.uploaded_on}
            Document: {self.document}
        """)

    def save_to_file(self):
        pass

    def do_service(self):
        print(f"{self.name} is being serviced.")
    
    



