import click
from helpers import init_db
from models.customers import Customer
from models.visits import Visit

# Initialize the database
init_db()

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
def cli_add_customer(name, email, phone):
    """Add a new customer."""
    Customer.add_customer(name, email, phone)

@customer.command("view")
def cli_view_customers():
    """View all customers."""
    customers = Customer.view_customers()
    if customers:
        for customer in customers:
            click.echo(customer)
    else:
        click.echo("No customers found.")

@customer.command("delete")
@click.argument("customer_id", type=int)
def cli_delete_customer(customer_id):
    """Delete a customer."""
    Customer.delete_customer(customer_id)

# ----- Visit Commands -----
@cli.group()
def visit():
    """Manage visits."""
    pass

@visit.command("add")
@click.argument("customer_id", type=int)
@click.argument("visit_date")
@click.argument("amount_paid", type=float)
def cli_add_visit(customer_id, visit_date, amount_paid):
    """Add a new visit."""
    Visit.add_visit(customer_id, visit_date, amount_paid)

@visit.command("view")
@click.argument("customer_id", type=int)
def cli_view_visits(customer_id):
    """View visits for a specific customer."""
    visits = Visit.view_visits(customer_id)
    if visits:
        for visit in visits:
            click.echo(visit)
    else:
        click.echo("No visits found for this customer.")

@visit.command("delete")
@click.argument("visit_id", type=int)
def cli_delete_visit(visit_id):
    """Delete a visit."""
    Visit.delete_visit(visit_id)

if __name__ == "__main__":
    cli()
