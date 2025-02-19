import random
#Guess the three digit number
#Randomchange
#Print Pico when you have a correct digit in the wrong place
#Print Fermi when you have a correct digit in the correct place
#Print Bagels if your guess has no correct digits
#10 tries total
number=random.randrange(100, 999, 1)
guestcount=0
startgame=input("Want to play a game of Bagel?")
while True:
    pico=False
    if startgame != "No":
        #number=random.randrange(100, 999, 1)
        number=str(number)
        print(number)
        while True:
            guess=1
            try:
                guess=int(input("Enter you guess (3 digit number): "))
            except:
                print("That's not a three digit number!")
            if guess < 100:
                print("It has to be a three digit number!")
            if guess > 999:
                print("That's too big of a number!")
            elif guess >=100 and guess <= 999:
                break
        guess=str(guess)
        guestcount += 1
        if guess[0] == number[0] or guess[1] == number[1] or guess[2] == number[2]:
            print("Fermi")
        if guess[1] == number[0] and guess[1] != number[1] or guess[2] == number[0] and guess[2] != number[2]:
            print("Pico")
            pico=True
        if guess[0] == number[1] and guess[0] != number[0] or guess[2] == number[1] and guess[2] != number[2]:
            print("Pico")
        if guess[0] == number[2] and guess[0] != number[0] or guess[1] == number[2] and guess[1] != number[1]:
            print("Pico")
        print(f"That's {guestcount}! You only have {10 - guestcount} left!")
        if guess == number:
            break
        if guestcount >= 10:
            print("Game over, you lost!")
            break
#        break
#    else:
#        break   
