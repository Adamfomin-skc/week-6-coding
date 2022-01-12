# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v1
# Purpose: A program to demonstrate the single if statement

import random
mylist= ['apple','cherry','orange','banana']

number = random.choice(mylist)
print(number)

guess = str(input("guess my favourite fruit: "))

# Evaluate the condition
if guess == number:
    print("Your guess was correct")
    print("Well done!")

print("Goodbye")