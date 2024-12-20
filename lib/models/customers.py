#customers.py
from helpers import get_connection

class Customer:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone})"
    
    @classmethod
    def add_customer(cls, name, email, phone):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()
            print("Customer added successfully!")
        except Exception as e:
            print(f"Error adding customer: {e}")
        finally:
            conn.close()

    @classmethod
    def view_customers(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        conn.close()
        return [Customer(*row) for row in rows]

    @classmethod
    def delete_customer(cls, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
            conn.commit()
            print(f"Customer with ID {customer_id} deleted successfully!")
        except Exception as e:
            print(f"Error deleting customer: {e}")
        finally:
            conn.close()
