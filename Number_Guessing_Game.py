import random
guess = int(input(f"What is your guess? "))
secret_number = random.choice(range(1,6))

while guess != secret_number:
    other_guess = (int(input(f"Wrong answer, please try again: ")))
    guess = other_guess
    if guess < 1 or guess > 5:
        print("Please guess between 1 to 5")
        continue
    elif guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
print("Congrats! your guess is correct")