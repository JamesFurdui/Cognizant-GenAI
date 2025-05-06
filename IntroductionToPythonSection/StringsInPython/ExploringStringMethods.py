#To run the different tasks cleanly, comment out the other two tasks 
# then run the program in order to 'declutter' the output

#Task 1
str = "Python is amazing!"

firstWord = str[0:6]
amazingWord = str[10:17]
reversedStr = str[::-1]

print(reversedStr)

#Task 2
str2 = " hello, python world! "

str2 = str2.strip() 
str2 = str2.capitalize()  
str2 = str2.replace("world", "universe") 
str2 = str2.upper()  

print(str2)

#Task 3
user_input = input("Enter a word: ")

user_reversed = user_input[::-1] 

if (user_input == user_reversed):
    print(f"{user_input} is a palindrome")
else:
    print(f"{user_input} is not a palindrome")