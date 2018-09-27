#!/usr/bin/env python3

# Taking input any number
print("Calculate table of a Number Quickly")
number = int(input("Enter number :"))

# Implementing in for loop from 1 to 10
print("Table of Number {}".format(number))
for i in range(1,11):
	print("{}x{} = {}".format(number,i,number*i))
