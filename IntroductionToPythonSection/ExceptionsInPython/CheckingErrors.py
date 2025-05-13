# Task 1 - Understanding Python Exceptions
try: 
    user_input = int(input("Enter a number: "))
    print(100 / user_input)
except ValueError:
    print("Not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")



# Task 2 - Types of Exceptions
# IndexError - Raised when trying to access an element that is out of range
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 does not exist (list has only 3 elements)
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError - Raised when trying to access a dictionary key that does not exist
try:
    my_dict = {"name": "Alice", "age": 30}
    print(my_dict["height"])  # 'height' key is not in the dictionary
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError - Raised when an operation or function is applied to an object of inappropriate type.
try:
    result = "Age: " + 25  # Can't add string and integer directly
except TypeError:
    print("TypeError occurred! Unsupported operand types.")



# Task 3 - Using try...except...else...finally
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Enter a valid number.")
else:
    print(f"The result is {result}.")
finally:
    print("Program finished successfully.")