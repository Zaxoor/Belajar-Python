import random
Choice = ["Rock", "Paper", "Scissors"]
play_again = "Y"
while str(play_again) == "Y":
    user = (input("Choose your hand: "))
    computer = (random.choice(Choice))
    print("You choose: " + str(user))
    print("The Computer choose: " + computer)
    if str(user) == computer:
        print("Result : Draw")
    elif str(user) == "Rock" and computer == "Scissors":
        print("Result : You win!")
    elif str(user) == "Paper" and computer == "Rock":
        print("Result : You win!")
    elif str(user) == "Scissors" and computer == "Paper":
        print("Result: You win!")
    else: 
        print("Result : You lose!")
    play_again = input("Want to play again(Y/N)? ")
    print("")
print("Thank you for playing!")