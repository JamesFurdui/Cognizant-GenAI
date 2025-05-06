# A very basic Password Checker. A small 'password strength meter' with basic implementation
# has been added. A much more advanced version could be implemented but this gets the basic
# gist of how a strength meter should act and respond based on what values were given.

goodPassword = False
user_input = input("Please provide a new password: ")
passwordStrengthMeter = 10

while goodPassword == False:
    if len(user_input) < 8:
        passwordStrengthMeter = 0
        print(f"Your password needs to be at least 8 characters long. It gets a {passwordStrengthMeter} out of 10!")
        user_input = input("Please provide a new password: ")
    elif not any(char.isupper() for char in user_input):
        passwordStrengthMeter = 5
        print(f"Your password needs at least one uppercase letter. It gets a {passwordStrengthMeter} out of 10!")
        user_input = input("Please provide a new password: ")
    elif not any(char.islower() for char in user_input):
        passwordStrengthMeter = 5
        print(f"Your password needs at least one lowercase letter. It gets a {passwordStrengthMeter} out of 10!")
        user_input = input("Please provide a new password: ")
    elif not any(char.isdigit() for char in user_input):
        passwordStrengthMeter = 7
        print(f"Your password needs at least one digit. It gets a {passwordStrengthMeter} out of 10!")
        user_input = input("Please provide a new password: ")
    elif all(char.isalnum() for char in user_input):
        passwordStrengthMeter = 9
        print(f"Your password needs at least one special character. It gets an {passwordStrengthMeter} out of 10! So Close!")
        user_input = input("Please provide a new password: ")
    else:
        passwordStrengthMeter = 10
        goodPassword = True
        print(f"Your password is strong! 💪 It gets a {passwordStrengthMeter} out of 10!")