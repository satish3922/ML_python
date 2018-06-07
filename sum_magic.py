#!/bin/env python3

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
