#!/usr/bin/env python3

# Defining old value of email and password
email_old = "admin@mywbut.com"
pass_old = "12345"

# Taking new value of email and Password
email = input("Your E-mail : ")
password = input("Your Password : ")

# Checking if Password is Incorrect or Not
if (email==email_old) and (password!=pass_old):
	print("You have entered wrong password")
	if input("Do you forgot your password ? ('Y'|'N') : ") == 'N':
		if (input("Try Password Again : ")==pass_old): # Giving one more attempt
			print("Congratulation !!!")
			print("You are In")
		else:
			print("F*** off")
	else:
		print("Contact System Administrator")

# Checking if email is Incorrect or Not
elif (email!=email_old) and (password==pass_old):
	print("You have entered wrong Email")
	if input("Do you forgot your Email ? ('Y'|'N') : ") == 'N':
		if (input("Try Email Again : ")==email_old): # Giving one more attempt
			print("Congratulation !!!")
			print("You are In")
		else:
			print("F*** off")
	else:
		print("Contact System Administrator")

# Checking if both Email and Password is Incorrect or Not
elif (email==email_old) and (password==pass_old):
	print("Congratulation !!!")
	print("You are In")

else:
	print("You have entered wrong email and password !!!")
	print("You are out")
