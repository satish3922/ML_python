#!/bin/env python3

import random
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
