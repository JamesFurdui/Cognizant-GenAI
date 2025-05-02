#Declares a name, age, and height variable with their respective values
name = "Alex"
age = 25
height = 5.9

#Declares num1 and num2 with an integer value
num1 = 37
num2 = 9

#Prints the modulo of num1 and num2
print("The modulo of 37 and 9 is", num1 % num2)
#Prints the name, age, and height using declared variables
print("Hey there, my name is " + name + ", I am " + age + ", and I am" + height + " feet tall")

#Recieves input from a user
user_input = int(input("Give a number: "))
#Depending on the value given from the user, it will print a different output
if user_input > 0:
    print("This number is positive. Awesome!")
elif user_input < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")