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

# ----- Customer Commands -----
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