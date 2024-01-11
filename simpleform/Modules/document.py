class Document:
    def __init__(self, car, doc_type, file_name, uploaded_on):
        self.car = car
        self.doc_type = doc_type
        self.file_name = file_name
        self.uploaded_on = uploaded_on

    def print_details(self):
        print(f"""
               Document Details
            Document Type: {self.doc_type}
            Car: {self.car.name} ({self.car.reg_no})
            Uploaded On: {self.uploaded_on}
            File Name: {self.file_name}
        """)

    def save_to_file(self):
        # Implement saving document details to a file
        pass
