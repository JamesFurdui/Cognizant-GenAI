# Project: About Menu

from turtle import *

# Calculate the factorial of a number using recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
# Calculate the nth Fibonacci number using recursion
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
# Draw a tree using recursion and turtle graphics
def fractalPattern(length, level):
    if level == 0:
        return

    forward(length)
    right(30)
    fractalPattern(length * 0.7, level - 1)
    left(60)
    fractalPattern(length * 0.7, level - 1)
    right(30)
    backward(length)

def positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Enter a valid number.")


# Main loop which takes in user input and runs all the provided functions above with some error-checking
user_input = 0
while user_input != 4:
    print("Welcome to the Recursive Artistry Program! Choose an option:")
    print("1. Calculate Factorial\n2. Find Fibonacci\n3. Draw a Recursive Fractal\n4. Exit")
    
    try:
        user_input = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a number from 1 to 4.")
        continue

    if user_input == 1:
        number = positive_int("Please provide a number to calculate: ")
        print(f"The factorial of {user_input} is {factorial(user_input)}")
    elif user_input == 2:
        number = positive_int("Provide the position for the fibonacii number: ")
        print(f"The number {user_input}'s Fibonacci number is {fibonacci(user_input)}")
    elif user_input == 3:
        left(90)
        fractalPattern(100, 5)
        done()
    elif user_input == 4:
        break

