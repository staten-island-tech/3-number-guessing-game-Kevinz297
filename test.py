import random

number_to_guess = random.randint(1, 10)
guess = 0
guess_history = []

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        guess_history.append(guess)
        print("Your guesses so far:", guess_history)

print("Congratulations! You've guessed the number.")
print("Your guess history:", guess_history)