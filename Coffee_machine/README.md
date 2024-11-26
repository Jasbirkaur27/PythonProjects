## Coffee Machine Project - README
### Overview <br>
The Coffee Machine project simulates a coffee machine that allows users to order drinks, manage resources (water, milk, coffee), and process payments. It involves different Python files that together handle menu display, resource management, and monetary transactions.<br>
This folder contains the following Python files:<br>
**main.py**- The main entry point for running the coffee machine application.<br>
**menu.py** - Contains the Menu class, which lists available drinks and their prices.<br>
**money_machine.py** - Handles the processing of payments and checking if enough money is provided for an order.<br>
**coffee_maker.py** - Manages the resources of the coffee machine, checking if enough ingredients are available to make a drink and updating the inventory after making a coffee.<br>
### Files and Description 
**1. main.py**<br>
This is the main file that runs the coffee machine application. It continuously interacts with the user, asks for drink orders, checks if there are enough resources, processes payments, and makes the coffee.<br>
Key Features:<br>
Asks the user for their order.<br>
Provides a report of available resources (water, milk, coffee).<br>
Allows the user to turn off the machine or order a drink.<br>
Checks if sufficient resources are available for the selected drink.<br>
Processes the payment and updates resources after making the coffee.<br>


**2. menu.py**
This file defines the Menu and MenuItem classes that list the available drinks and their corresponding prices.<br>
Key Features:<br>
Displays a list of available drink options.<br>
Allows searching for a specific drink by its name.<br>

**3. money_machine.py**
The MoneyMachine class is responsible for managing the payment system. It checks if the user has inserted enough money for their selected drink and handles the payment transaction.<br>
Key Features:<br>
Reports how much money has been inserted.<br>
Validates if the user has provided sufficient funds for the drink order.<br>
Processes the payment and returns the change if needed.<br>
**4. coffee_maker.py**
This class models the coffee machine itself, keeping track of the ingredients (water, milk, coffee). It checks if there are enough resources to make a selected drink and deducts the necessary ingredients from the available inventory.<br>

Key Features:<br>
Reports the available ingredients (water, milk, coffee).<br>
Checks if there are enough ingredients for a drink.<br>
Makes the coffee by deducting the required ingredients from the inventory.<br>
