import random 

Uwins = 0 
Cwins = 0

ops = ["ROCK","PAPER","SCISSORS"]

print("\n****** WELCOME TO ROCK,PAPER,SCISSORS GAME ******")

while True:
    Upick = (input("\nEnter Rock, Paper or Scissors or Q to quit: ")).upper()

    if Upick == "Q":
        break

    if Upick not in ops:
        print("\nInvalid Input, please enter a valid option")
        continue

    c = random.randint(0,2)

    Cpick = ops[c]

    print("\nComputer picked", Cpick)

    if Upick == "ROCK" and Cpick == "SCISSORS":
        print("\nYou win!")
        Uwins += 1
    elif Upick == "PAPER" and Cpick == "ROCK":
        print("\nYou win!")
        Uwins += 1
    elif Upick == "SCISSORS" and Cpick == "PAPER":
        print("\nYou win!")
        Uwins += 1
    else :
        print("\nYou Lost")
        Cwins += 1

print("\nYou won", Uwins ,"times.")
print("\nComputer won", Cwins ,"times.")

print("\n********** THANKYOU FOR PLAYING :) **********\n")