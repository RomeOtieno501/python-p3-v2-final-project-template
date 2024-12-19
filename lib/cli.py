import click
from helpers import init_db, get_connection
from models.customers import Customer
from models.visits import Visit

# Initialize the database
init_db()

# Customer CLI Group
@click.group()
def cli():
    """Hotel Management System CLI"""
    pass

# Customer Commands 
@cli.group()
def customer():
    """Manage customers."""
    pass

@customer.command("add")
@click.argument("name")
@click.argument("email")
@click.argument("phone")
def add_customer(name, email, phone):
    """Add a new customer."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        click.echo("Customer added successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        conn.close()

@customer.command("view")
def view_customers():
    """View all customers."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            click.echo(Customer(*row))
    else:
        click.echo("No customers found.")

@customer.command("delete")
@click.argument("customer_id", type=int)
def delete_customer(customer_id):
    """Delete a customer."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    conn.close()
    click.echo("Customer deleted successfully.")


# ----- Visit Commands -----
@cli.group()
def visit():
    """Manage visits."""
    pass

@visit.command("add")
@click.argument("customer_id", type=int)
@click.argument("visit_date")
@click.argument("amount_paid", type=float)
def add_visit(customer_id, visit_date, amount_paid):
    """Add a new visit."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO visits (customer_id, visit_date, amount_paid) VALUES (?, ?, ?)",
                       (customer_id, visit_date, amount_paid))
        conn.commit()
        click.echo("Visit added successfully!")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        conn.close()

@visit.command("view")
@click.argument("customer_id", type=int)
def view_visits(customer_id):
    """View visits for a specific customer."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM visits WHERE customer_id = ?", (customer_id,))
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            click.echo(Visit(*row))
    else:
        click.echo("No visits found for this customer.")

@visit.command("delete")
@click.argument("visit_id", type=int)
def delete_visit(visit_id):
    """Delete a visit."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visits WHERE id = ?", (visit_id,))
    conn.commit()
    conn.close()
    click.echo("Visit deleted successfully.")



if __name__ == '__main__':
    cli()