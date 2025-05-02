# Take an input from the user asking how old they are
age = int(input("How old are you? "))

# If else statement which either prints that they are eligible. Or if they are under the age of
# 18, it will print that they are not eligible yet and provide how many years they have left.
# Added a case for if they are 17 years old, it will provide the correct grammar. 
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    if age == 17:
        print("Oops! You're not eligible yet. But hey, only " + str(18 - age) + " year to go!")
    else:
        print("Oops! You're not eligible yet. But hey, only " + str(18 - age) + " years to go!")