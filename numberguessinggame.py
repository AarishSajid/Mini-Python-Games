import random 

print("******* Welcome To Number Guessing Game *******")

while True:
    top = input("\nEnter the Top Range for the random number : ")

    if top.isdigit():
        top = int(top) 

        if top <= 0:
            print("\nplease enter a number greater then 0")
            continue
        else:
            break
    else:
        print("\nplease enter a number :)")
        continue


num = random.randrange(top)

while True:
    guess = 1
    guess = guess + 1
    user = input("\nPlease enter your guess : ")

    if user.isdigit():
        user = int(user) 
    else:
        print("\nplease enter a number")
        continue

    if user == num:
        print("\nYAY! You got it ")
        break
    else :
        if user > num:
            print("\nYour guess is higher the number")
            continue
        elif user < num:
            print("\nYour guess is lower than the number")
            continue

print("\nYou got the number in",guess,"tries")

print("\n************ Thankyou for Playing **************\n")