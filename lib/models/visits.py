from helpers import get_connection

class Visit:
    def __init__(self, id, customer_id, visit_date, amount_paid):
        self.id = id
        self.customer_id = customer_id
        self.visit_date = visit_date
        self.amount_paid = amount_paid

    def __repr__(self):
        return f"Visit(ID: {self.id}, Customer ID: {self.customer_id}, Date: {self.visit_date}, Amount Paid: {self.amount_paid})"
    
    @classmethod
    def add_visit(cls, customer_id, visit_date, amount_paid):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO visits (customer_id, visit_date, amount_paid) VALUES (?, ?, ?)",
                (customer_id, visit_date, amount_paid),
            )
            conn.commit()
            print("Visit added successfully!")
        except Exception as e:
            print(f"Error adding visit: {e}")
        finally:
            conn.close()

    @classmethod
    def view_visits(cls, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM visits WHERE customer_id = ?", (customer_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Visit(*row) for row in rows]

    @classmethod
    def delete_visit(cls, visit_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM visits WHERE id = ?", (visit_id,))
            conn.commit()
            print(f"Visit with ID {visit_id} deleted successfully!")
        except Exception as e:
            print(f"Error deleting visit: {e}")
        finally:
            conn.close()
