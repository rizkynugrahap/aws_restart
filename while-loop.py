"""
Working with a while loop
"""

#Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


#Importing random and writing a while loop
import random
number = random.randint(1,10)
isGuestRight = False

while isGuestRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuestRight = True
    else:
        print("You guessed {}. Sorry, that isn't it, Try again.".format(guess))
        
"""
Pseudocode

if the user has not guessed the correct answer. enter the loop
ask the user for a guess
is the guess the correct number?
if the correct guess, tell the user it was the correct guess and exit the lop
if the wrong guess, tell the user it was the wrong guess and continue the loop

"""