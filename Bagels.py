import random
while True:
    guestcount=0
    startgame=input("Want to play a game of Bagels? ")
    number1=random.randrange(0, 9, 1)
    number2=random.randrange(0, 9, 1)
    number3=random.randrange(0, 9, 1)
    number1=str(number1)
    number2=str(number2)
    number3=str(number3)
    number=number1+number2+number3
    gamewin=False
    rules=True
    if startgame == "No":
            break
    while True:
        pico=False
        Fermi=False
        if startgame != "No":
            if rules == True:
                print("Okay, here's how it works:")
                print("I will say Pico when you have a correct digit in the wrong place")
                print("I will say Fermi when you have a correct digit in the correct place")
                print("I will say Bagels if your guess has no correct digits")
        #number=random.randrange(100, 999, 1)
        #number=str(number)
            #print(number)
            while True:
                rules=False
                guess=(input("Enter you guess (3 digit number): "))
                if not guess.isdecimal() or len(guess) != 3:
                    print("It must be a three digit number!")
                else:
                    break
                #if (len(guess)) <= 3:
                    #print("It has to be a three digit number!")
                #if (len(guess)) >= 3:
                    #print("That's too big of a number!")
                #elif (len(guess)) == 3:
                    #break
            #guess=str(guess)
            pico=False
            Fermi=False
            if guess == number:
                print("You win!")
                gamewin=True
                break
            if gamewin==True:
                restart=input("Want to play again?")
                if restart != "Yes":
                    break
            guestcount += 1
            if guess[0] == number[0] or guess[1] == number[1] or guess[2] == number[2]:
                print("Fermi")
                Fermi=True
            if guess[1] == number[0] and guess[1] != number[1] or guess[2] == number[0] and guess[2] != number[2]:
                print("Pico")
                pico=True
            elif pico==False and guess[0] == number[1] and guess[0] != number[0] or guess[2] == number[1] and guess[2] != number[2]:
                print("Pico")
                pico=True
            elif pico==False and guess[0] == number[2] and guess[0] != number[0] or guess[1] == number[2] and guess[1] != number[1]:
                print("Pico")
                pico=True
            elif Fermi == False and pico == False:
                print("Bagels")
            print(f"That's {guestcount}! You only have {10 - guestcount} left!")
            if guestcount >= 10:
                print("Game over, you lost!")
                break