import rendom

nuomber_to_guess = random.randint(1, 10)
guess = 0
gess_history = []

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number_to_guess:
        print("Too low try again stupid!")
    elif guess > number_to_guess:
        print("Too high on coke!")
    else:
        print("Congratulations! You've guessed the number.")
    guess_history.append(guess)
print("Congratulations! You've guessed the numbe.")
for i in range(len(guess_history)):
print(f"Guess {i + 1}: {guess_history[i]}")
print("Your guess history:", guess_history)
