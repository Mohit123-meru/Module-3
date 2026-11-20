import random

while True:
    ca = ["Rock", "Paper", "Scissors"]
    user = input ("Ennter any option between Rock, Paper, and Scissors : ")
    computer = random.choice(ca)
    if computer == user:
        print ("It's a tie!")
    elif user == "Paper":
        if computer == "Rock":
            print("You win!")
        else :
            print ("You lose...")
    elif user == "Rock":
        if computer == "Paper":
            print("You lose...")
        else :
            print ("You win!")
    elif user == "Scissor":
        if computer == "Paper":
            print ("You win!")
        else :
            print ("You lose...")
    con = input ("Do you want to continue? (yes or no) : ")
    if con != "yes":
        break
