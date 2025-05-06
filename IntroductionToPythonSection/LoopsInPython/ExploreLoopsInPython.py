#To run all the provided tasks cleanly, comment out the other two tasks then run 
#the program in order to 'declutter' the output

#Task 1
#Decrements the user input by one each time it iterates
print("Please provide a number: ")
user_input = int(input())
while user_input > 1:
    user_input -= 1
    print(user_input)
print("Blast off!")

#Task 2
#Sets the range for what multiplication to do (1, 11)
#Prints out the user input and i then multiplies them both in the print function as the 'i'
#is always incrementing till 10
print("Please provide a number: ")
user_input = int(input())
for i in range(1, 11):
    print(f"{user_input} x {i} = {user_input * i}")

#Task 3
#Set a base factorial value so the first iteration of the for loop would work (cant multiply by 0 or by a value that isnt there ;-;)
#The for loop continually multiplies the factorialvalue by i and returns that as the answer
factorialvalue = 1
print("Please provide a number: ")
user_input = int(input())
for i in range(1, user_input + 1):
    factorialvalue *= i
print(f"The factorial of {user_input} is {factorialvalue}")