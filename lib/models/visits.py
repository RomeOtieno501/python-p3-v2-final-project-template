class Visit:
    def __init__(self, id, customer_id, visit_date, amount_paid):
        self.id = id
        self.customer_id = customer_id
        self.visit_date = visit_date
        self.amount_paid = amount_paid

    def __repr__(self):
        return f"Visit(ID: {self.id}, Customer ID: {self.customer_id}, Date: {self.visit_date}, Amount Paid: {self.amount_paid})"
