print(" HELLO USER! YOU ARE READY TO PLAY GAME IF YES PRESS ENTER ")
input()

print("NOTE : YOU HAVE UNLIMITED CHANCE TO GUESS THE NUMBER ")

import random

level = input("ENTER YOUR COMFERTABLE LEVEL EASY / MEDIUM / HARD = ")

a1 = random.randint(1, 100)
a2 = random.randint(1,500)
a3 = random.randint(1,1000)

guess = int(input("ENTER YOUR GUESS = "))

if level == "easy" :
    while a1 != guess :
        if a1 > guess :
            print("Guess Higer!")
        if a1 < guess :
            print("Guess lower!")
        guess = int(input("Guess again = "))

if level == "medium" :
    while a2 != guess :
        if a2 > guess :
            print("Guess Higer!")
        if a2 < guess :
            print("Guess Lower!")
        guess =  int(input("Guess again = "))

if level == "hard":
    while a3 != guess :
        if a3 > guess :
            print("Guess Higer!")
        if a3 < guess :
            print("Guess lower!")
        guess = int(input("Guess again = "))

if a1 == guess :
    print("Nice, You win")

if a2 == guess :
    print("Good, You Win")

if a3 == guess :
    print("Excellent, You Win")