# Python Coffee Project

Python Coffee Project is a Python-based command-line coffee machine simulation. The project recreates the core functionality of a coffee vending machine, allowing users to select drinks, process payments, check available resources, and receive their order.

The project focuses on strengthening Python programming fundamentals through a practical application involving functions, conditional logic, data structures, resource management, and user interaction.

## Features

* Multiple coffee options
* Resource availability management
* Ingredient consumption tracking
* Coin-based payment system
* Payment validation
* Change calculation
* Resource availability report
* Machine shutdown functionality
* User-friendly command-line interface

## Tech Stack

* Python
* Python Standard Library

## Project Structure

```text id="q3b8m2"
python-coffee-project/
├── main.py
├── menu.py
├── coffee_maker.py
├── money_machine.py
└── README.md
```

## How It Works

The application simulates the workflow of a coffee vending machine.

Users can select a coffee from the available menu. The machine checks whether the required ingredients are available before processing the order.

After selecting a drink, the user enters coins as payment. The application calculates the total amount, verifies whether sufficient payment was provided, and calculates the appropriate change.

Once the transaction is successful, the required ingredients are deducted from the machine's available resources and the selected coffee is prepared.

## Available Commands

The application supports different commands for interacting with the machine, including:

* Selecting available coffee drinks
* `report` — Display current machine resources and money
* `off` — Shut down the machine

## Core Concepts

This project demonstrates practical experience with:

* Python programming
* Functions
* Conditional statements
* Loops
* Dictionaries
* Object-oriented programming
* User input handling
* Data validation
* Resource management
* Payment processing
* Modular code organization

## Application Flow

```text
Select Coffee
      |
      v
Check Resources
      |
      v
Process Payment
      |
      v
Validate Payment
      |
      v
Calculate Change
      |
      v
Prepare Coffee
      |
      v
Update Resources
```

## Learning Outcomes

This project provides hands-on practice with designing a small real-world system using Python. It demonstrates how separate components can work together to manage resources, process transactions, validate user input, and maintain application state.

## Live Demo

[View the Live Demo on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7346176168099725312/)

## Future Improvements

* Add a graphical user interface
* Add more beverage options
* Add customizable coffee recipes
* Add inventory restocking functionality
* Add transaction history
* Add daily sales reports
* Add persistent data storage
* Add improved input validation
* Add administrator controls
* Add database integration

## Author

**Sadaf Javed**

Software Engineering Student and Web Developer

## Connect With Me

[LinkedIn — Sadaf Javed](https://www.linkedin.com/in/sadaf-javed/)
