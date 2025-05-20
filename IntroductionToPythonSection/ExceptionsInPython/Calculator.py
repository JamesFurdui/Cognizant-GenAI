# Project: Calculator with Exception Handling
import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

user_value = 0
while True:
    try:
        user_value = int(input("Welcome to the Error-Free Calculator! Choose an operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\nEnter your choice (1-5): "))

        if user_value < 1 or user_value > 5:
            raise ValueError("Please provide a valid number. (1-5)")

        if user_value == 5:
            print("Thank you for using the calculator!")
            break

        # Helper to get the two numbers with validation
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            logging.error("ValueError: Numeric input not provided.")
            continue

        # Finally perform the operations if no Errors present themselves
        if user_value == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        if user_value == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        if user_value == 3:
            print(f"{num1} x {num2} = {num1 * num2}")
        if user_value == 4:
            try:
                result = num1 / num2 
            except ZeroDivisionError as zde:
                print("Unable to divide by zero.")
                logging.error(f"ZeroDivisionError occurred: {zde}")
            else:
                print(f"{num1} / {num2} = {result}")
            finally:
                print("Division operation attempted.\n")

    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError occured: {ve}")
