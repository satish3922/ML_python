#!/usr/bin/env python3

import sys,time,random
count=0
# Creating Database
# sample -> "email":["name","password"]
mydb={"rudra@gmail.com":["rudra","123546"]}

# ======================User Menu after LOGIN=========================================

#=====================================================================================
# Game Menu
def game_menu():
	print("-------------------------")
	print("1 : Guess Game\n2 : Bull & Cow Game\n3 : Magic Sum Game\n4 : Logout")
	print("-------------------------")
	game_input=(input("Choice : "))
	if game_input=='1':
		guess_game()
	elif game_input=='2':
		bull_game()
	elif game_input=='3':
		magic_sum()
	else:
		sys.exit()
#=====================================================================================


#=====================================================================================
# Define guess_game Function
def guess_game():
	global count
	level=level_guess()
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
	mood=input("-------------------------\npress 1 : Play Again\npress 2 : Game Menu\npress 3 : logout\n-------------------------\nChoice :")
	if(mood=='1'):
		guess_game()
	elif(mood=='2'):
		game_menu()
	else:
		sys.exit()

# Asking for level Function for guess_game
x1=random.randint(1,10)
x2=random.randint(10,100)
x3=random.randint(100,999)
def level_guess():
	print("Choose Level\n1 : Easy (1 digit)\n2 : Medium (2 digit)\n3 : Hard (3 digit)")
	level=input("choose : ")
	if level=='1':
		return x1
	elif level=='2':
		return x2
	elif level=='3':
		return x3
	else:
		game_menu()
#======================================================================================

#======================================================================================
# Define Bull game
def bull_game():
	number = str(random.randint(999,9999))
	user_input = input("Enter the 4 digit number  : ")
	cow=0
	bull=0
	for i in range(1,len(user_input)+1):
		if user_input[i-1] in number[i-1]:
			cow=cow+1
		else:
			bull=bull+1
	print("{} cow, {} Bull ".format(cow,bull))
	mood=input("-------------------------\npress 1 : Play Again\npress 2 : Game Menu\npress 3 : logout\n-------------------------\nChoice :")
	if(mood=='1'):
		bull_game()
	elif(mood=='2'):
		game_menu()
	else:
		sys.exit()

#======================================================================================

#======================================================================================
# Define Magic sum Function
def magic_sum():
	# Program of magic Addition
	#Taking input of 1st Number
	num1 = int(input("Enter 1st Number :"))
	#Calculating Magic Sum (result = add 2 before num-2)
	result1 = '2' + str(num1 - 2)
	print("User : ",num1)
	print("User :  *****")
	print("Comp :  *****")
	print("User :  *****")
	print("Comp :  *****")
	print("=============")
	print("Sum : ",result1)
	print(" ")

	#Taking input of 2nd Number
	num2=int(input("Enter 2nd Number :"))
	#Calculating 2nd result by (each digit in num2 will be subtracted from 9)
	result2 = int(len(str(num2))*'9') - num2
	print("User : ",num1)
	print("User : ",num2)
	print("Comp : ",result2)
	print("User :  *****")
	print("Comp :  *****")
	print("=============")
	print("Sum : ",result1)
	print(" ")

	#Taking input of 3rd Number
	num3=int(input("Enter 3rd Number :"))
	#Calculating 2nd result by (each digit in num2 will be subtracted from 9)
	result3 = int(len(str(num3))*'9') - num3
	print("User : ",num1)
	print("User : ",num2)
	print("Comp : ",result2)
	print("User : ",num3)
	print("Comp : ",result3)
	print("=============")
	print("Sum : ",result1)
	print(" ")
	mood=input("-------------------------\npress 1 : Play Again\npress 2 : Game Menu\npress 3 : logout\n-------------------------\nChoice :")
	if(mood=='1'):
		bull_game()
	elif(mood=='2'):
		game_menu()
	else:
		sys.exit()
#======================================================================================
#=====================================================================================
# Define Menu Function
def menu():
	print("Press 1 : Login here\nPress 2 : Register here\nPress 3 : Exit Program")
	print("-------------------------")
	menu_input=input("Enter Your Choice : ")
	if menu_input=='1':
		# Calling Login Function
		login()
	elif menu_input=='2':
		register()
	else:
		sys.exit()
#=====================================================================================

#=====================================================================================
# Define Login function
def login():
	global mydb   # Defining mydb as global variable
	print("==== LOGIN FORM ====")
	# Taking Input
	email_for_login=input("E-mail : ")
	password_for_login=input("Password : ")
	# Verifying Credentials
	for i in mydb:
		if(email_for_login==i) and (password_for_login==mydb[i][1]): # checking for wrong email & password 1 and 1 = 1
			time.sleep(1)
			print("\nSuccessfully Logged In")
			print("Welcome {}".format(mydb[i][0].upper()))
			print("-------------------------")
			game_menu()

		elif(email_for_login==i):  # checking for wrong password 1 or 0 = 1
			if(password_for_login==mydb[i][1]):
				time.sleep(1)
				print("\nSuccessfully Logged In")
				print("---Welcome {}---".format(mydb[i][0].upper()))
				print("-------------------------")
				game_menu()
			else:
				print("\nWrong password")
				if(input("\nTry Password Again : ")==mydb[i][1]):
					time.sleep(1)
					print("\nSuccessfully Logged In")
					print("---Welcome {}---".format(mydb[i][0].upper()))
					print("-------------------------")
				else:
					print("\nContact Admin")
					print("-------------------------")
					menu()

		elif(password_for_login==mydb[i][1]):  # checking for wrong email
			if(email_for_login==i):
					time.sleep(1)
					print("\nSuccessfully Logged In")
					print("---Welcome {}---".format(mydb[i][0].upper()))
					print("-------------------------")
			else:
				print("\nWrong Email_id")
				print("-------------------------")
				print("\nPress 1 : Register\nPress 2 : Retry Login\n")
				choice=input("Choice : ")
				if(choice=='1'):
					register()
				elif(choice=='2'):
					login()
				else:
					menu()

		else:
			print("Wrong Credentials")
			print("-------------------------")
			print("Press 1 : Register\nPress 2 : Retry Login\n")
			choice=input("Choice : ")
			if(choice=='1'):
				register()
			elif(choice=='2'):
				login()
			else:
				menu()
#=====================================================================================

#=====================================================================================
# Define Register function
def register():
	global mydb
	print("==== REGISTRATION FORM ====")
	name_for_reg=input("Name : ")
	email_for_reg=input("E-mail : ")
	password_for_reg=input("Password (min 6) : ")
	for i in mydb:
		if(email_for_reg!=i) and (password_for_reg!=mydb[i][1]):   #
			if(check_pass(password_for_reg)==True) and (check_email(email_for_reg)==True):
				mydb[email_for_reg]=[name_for_reg,password_for_reg]
				print("\nSuccessfully Registered !\nLogin Now\n")
				print("-------------------------")
				time.sleep(1)
				login()
			elif(check(password_for_reg)!=True) or (check(password_for_reg)==True):
				print("Unsupported password")
				print("-------------------------")
				register()
			else:
				print("Unsupported Credentials")
				print("-------------------------")
				register()

		elif(email_for_reg!=i) or (password_for_reg==mydb[i][1]):  # 0 or 1 = 1
			if(check_email(email_for_reg)==True):
				mydb[email_for_reg]=[name_for_reg,password_for_reg]
				print("Successfully Registered !\nLogin Now\n")
				print("-------------------------")
				login()
			else:
				print("Unsupported Email")
				print("-------------------------")
				register()

		elif(email_for_reg!=i) and (password_for_reg==mydb[i][1]):
			print("User already exists")
			print("-------------------------")
			print("Try Login")
			login()

		elif(email_for_reg==i) and (password_for_reg!=mydb[i][1]):
			print("User already exists")
			print("-------------------------")
			print("Try Login")
			login()
#=====================================================================================

#=====================================================================================
# check password
def check_pass(password):
	if len(password)>=6:
		return True
	else:
		return False
# Check Email
def check_email(email):
	if '@' and '.' in email:
		return True
	else:
		return False

# calling menu function
print("-------------------------")
menu()
#=====================================================================================
