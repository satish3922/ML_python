#!/bin/env python3

import random
# Defining function Ask()
def ask():
	global count
	num = int(input("Guess again : "))
	if (num == x):
		count = count+1
		print("You Guessed right in {} attempt !!!".format(count))
	elif (num > x):
		count = count+1
		print("Try to Guess lesser number")
		ask()
	elif (num < x):
		count = count+1
		print("Try to Guess greater number ")
		ask()
	else :
		print("You failed")

x=random.randint(1,20)
count=0
number=int(input("Guess the number : "))

if (number == x):
	count = count+1
	print("You Guessed right in {} attempt !!!".format(count))
elif (number > x):
	count = count+1
	print("Try to Guess lesser number")
	ask()
elif (number < x):
	count = count+1
	print("Try to Guess greater number ")
	ask()
else :
	print("You failed")
