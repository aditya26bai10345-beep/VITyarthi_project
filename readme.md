# Simple Python Calculator

## Overview
This project is a command-line simple calculator developed to demonstrate core Python concepts. It is built as a modular application to fulfill the requirements of the VITyarthi "Build Your Own Project" evaluation. The application allows users to perform standard mathematical computations through an interactive terminal menu.

## Features
* Menu-driven user interface for selecting mathematical operations.
* Arithmetic operations: Addition, Subtraction, Multiplication, Division, Modulus, Power, and Square Root.
* Robust input validation that ensures only numeric values are processed.
* Custom error handling that prevents division by zero and rejects negative numbers for square root calculations.
* Continuous execution loop that allows repeated calculations until the user chooses to exit.

## Technologies/Tools Used
* **Language:** Python 3
* **Standard Libraries:** `math` (for square root operations)
* **Version Control:** Git / GitHub

## Steps to Install & Run the Project
1. Clone the repository to your local machine.
2. Ensure Python 3.x is installed.
3. Open a terminal or command prompt and navigate to the project directory.
4. Execute the main script by running: `python main.py`.

## Instructions for Testing
1. Launch the application and select option `1` (Addition). Enter `5` and `10` to verify the output is `15.0`.
2. Select option `4` (Division)[cite: 2]. Enter `10` and `0` to verify the system catches the `ZeroDivisionError` and displays the custom error message.
3. Select option `7` (Square Root)[cite: 2]. Enter `-4` to verify the system catches the `ValueError` and prevents the calculation.
4. At any input prompt, enter a letter (e.g., `a`) to verify the validation system catches the invalid type and prompts for digits only.

## Screenshots
*(Note: Add screenshots of the terminal menu and successful/failed operations here)*