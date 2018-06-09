#!/usr/bin/env python3

import random
count=0
# Define guess_game Function
def guess_game(level):
	global count
	user_input=int(input("Guess the number : "))
	while user_input != level:
		count = count+1
		if (user_input > level):
			print("Guess lesser number")
			user_input = int(input("Guess again : "))
		else:
			print("Guess greater number ")
			user_input = int(input("Guess again : "))
	print("Guessed right in {} attempts".format(count))

# Asking for level Function
x1=random.randint(1,10)
x2=random.randint(10,100)
x3=random.randint(100,999)
print("Choose Level\n1 : Easy (1 digit)\n2 : Medium (2 digit)\n3 : Hard (3 digit)")
level=input("choose : ")
if level=='1':
	guess_game(x1)
elif level=='2':
	guess_game(x2)
elif level=='3':
	guess_game(x3)
