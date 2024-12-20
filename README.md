# **Hotel Management System Database**

A simple command-line application to help hotel receptionists manage guest records efficiently.

By **Rome Otieno Ojuro**

## **Description**

This is a comprehensive hotel database system designed for hotel receptionists to simplify and streamline guest management. The application operates via a command-line interface (CLI) and enables receptionists to manage customer and visit records efficiently. This includes adding, viewing, and deleting customer and visit information. The tool supports accurate record-keeping, ensuring efficient customer service and resource tracking.

## **Features**

- View a list of customers and their details.

- Add new customers for better service tracking and customer care.

- Delete customer records to maintain accurate and up-to-date information.

- View visits associated with specific customers.

- Add new visit records for customers, including dates and payment information.

- Delete visit records to track resource utilization and manage records effectively.

## **How to Use**

### **Requirements**

- Python 3.8 or higher installed on your computer.

- SQLite for database management (included with Python).

- A code editor or terminal to run the application.

### **User Stories**

- **As a receptionist**, I want to view a list of all customers and their details.

- **As a receptionist**, I want to add new customers to the database for efficient customer management.

- **As a receptionist**, I want to delete customer records to keep the database accurate.

- **As a receptionist**, I want to view all visits associated with specific customers.

- **As a receptionist**, I want to add visit records to track customer activities.

- **As a receptionist**, I want to delete visit records when needed to maintain database accuracy.

## **Local Development**

### **Requirements**

- Python 3.8+ installed on your computer.

- SQLite (comes pre-installed with Python).

- Terminal/Command Line for running the application.

### **Installation Process**

1. Clone this repository using:

    ```bash
    git clone git@github.com:RomeOtieno501/python-p3-v2-final-project-template.git

    Or download a ZIP file of the project.

2. Navigate to the project directory:

    ```bash
    cd python-p3-v2-final-project-template


3. Install required dependencies:

    ```bash
    pipenv install 
    pip install click(if not already installed)
    pipenv shell 


4. Run the application:

    ```bash
    python cli.py

### **Example CLI Commands**

1. Add a Customer:
    ```bash
    python cli.py customer add "Dennis Kiboi" "denniskiboi2@gmail.com" "0755999222"

2. View Customers:

    ```bash 
    python cli.py customer view

3. Delete a Customer:

    ```bash
    python cli.py customer delete 1

4. Add a Visit:

    ```bash
    python cli.py visit add 1 "2024-12-25" 200.00

5. View Visits for a Customer:

    ```bash
    python cli.py visit view 1

6. Delete a Visit:

    ```bash
    python cli.py visit delete 1

## **Technologies Used**

- Python 3.8+: Core programming language.

- SQLite: Lightweight database for data storage and retrieval.

- Click: Python library for building command-line interfaces.

- Virtual Environments: Isolated Python environment for dependencies.

## Project Structure

project_root/
├── cli.py              # Main entry point for the command-line interface
├── helpers.py          # Helper functions for database initialization and connection
├── models/             # Directory for database models
│   ├── __init__.py     # Makes the directory a package
│   ├── customers.py    # Customer model and related database operations
│   └── visits.py       # Visit model and related database operations
└── hotel.db         # SQLite database file (auto-generated after init)

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

Email: otienorome2@gmail.com

## License

MIT License

Copyright © 2024 Emmanuel Mutugi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


