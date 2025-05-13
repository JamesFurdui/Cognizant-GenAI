# Task 1 - Writing Functions

def greet_user(name):
    print(f"Hello {name}! Thank you for applying!!", end=" ")

def add_numbers(num1, num2):
    print(f"The sum of these two numbers is {num1 + num2}.")

greet_user("James")
add_numbers(5, 10)


# Task 2 - Using Default Parameters

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3 - Functions with Variable Arguments

def make_sandwich(*args):
    print("Making a sandwich with the following ingredients:", *args, sep=" - ")
    print(*args)

make_sandwich("Lettuce", "Cheese", "Tomato")

# Task 4 - Understanding Recursion

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
def fibonacii(num):
    if num <= 1:
        return num
    else:
        return fibonacii(num - 1) + fibonacii(num - 2)
    
print(factorial(5))
print(fibonacii(6))