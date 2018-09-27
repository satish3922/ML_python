#!/usr/bin/env python3

import random
# Defining function Ask()
count=0
def ask(x):
	global count
	num = int(input("Guess again : "))
	if (num == x):
		count = count+1
		print("You Guessed in {} attempt".format(count))
	elif (num > x):
		count = count+1
		print("Guess lesser number")
		ask(x)
	elif (num < x):
		count = count+1
		print("Guess greater number ")
		ask(x)
	else :
		print("You failed")
# easy_guess Game
def guess_game(y):
	global count
	number=int(input("Guess the number : "))
	if (number == y):
		count = count+1
		print("You Guessed in {} attempt ".format(count))
	elif (number > y):
		count = count+1
		print("Guess lesser number")
		ask(y)
	elif (number < y):
		count = count+1
		print("Guess greater number ")
		ask(y)
	else :
		print("You failed")

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
else:
	game_menu()
