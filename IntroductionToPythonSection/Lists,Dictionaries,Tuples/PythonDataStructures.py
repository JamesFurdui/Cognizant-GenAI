# Comment out the other tasks when attempting to run the code.
# One thing to note is that in task 2, there are multiple implementations of
# attaining the keys and values using a loop with the last one being an AI implementation
# so please keep that in mind.

#############################
# Task 1: Working with Lists
#############################
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Original list: {fruits}")

fruits.append("rasberry")
print(f"After adding a fruit: {fruits}")

fruits.remove("apple")
print(f"After removing a fruit: {fruits}")

reversedFruits = fruits[::-1]
print(reversedFruits)

################################
# Task 2: Exploring Dictionaries
################################
aboutMe = {"name" : "James", "age" : 20, "city" : "Riverside"}
aboutMe["favorite color"] = "blue"
aboutMe["city"] = "Seattle"

#1 This is a much simpler implementation I discovered to attaining the keys and values
#without the use of a loop.
print(aboutMe.keys())
print(aboutMe.values())

#2 This is a second implementation I tried using loops
print("Keys: ", end="")
for i in aboutMe:
    print(i, end=" ")
print()
print("Values: " , end="")
for i in aboutMe:
    print(aboutMe[i], end=" ")

#3 This is a refined implementation I discovered using AI
print("Keys:", ", ".join(aboutMe.keys()))
print("Values:", ", ".join(str(value) for value in aboutMe.values()))

######################
# Task 3: Using Tuples
######################
favoriteThings = ("Interstellar", "Resonance by Home", "Percy Jackson Series")

print(f"Favorite things: {favoriteThings}")

try:
    favoriteThings[0] = "The Matrix"
except TypeError:
    print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(favoriteThings)}")



