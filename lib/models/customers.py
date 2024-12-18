class Customer:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone})"
