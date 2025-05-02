import random

number_to_guess = random.randint(1, 100)
counter = 0

print("Guess the number (between 1 and 100): ", end='')
user_input = int(input())

while number_to_guess != user_input:
    if user_input < number_to_guess:
        print(f"Guess the number (between 1 and 100): {user_input} Too low! Try again.")
    else:
        print(f"Guess the number (between 1 and 100): {user_input} Too high! Try again.")
    counter += 1
    if counter == 10:
        print(f"You were unable to guess the number {number_to_guess} in 10 guesses. Better luck next time!")
        break
    user_input = int(input("Guess the number (between 1 and 100): "))

if number_to_guess == user_input:
    print(f"Congratulations! You guessed the number {number_to_guess} in {counter + 1} attempts")