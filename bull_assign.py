#!/usr/bin/env python3

import random
cow=bull=count=0
data=[]  # Define a blank list for history of user_input
rand_num = str(random.randint(999,9999))
print(rand_num)
# Define check()
def check():
    user_input = input("Guess 4-digit no. : ")
    c=b=0
    for i in range(1,len(user_input)+1):
        if user_input[i-1] in rand_num[i-1]:
            c=c+1
    return(c,b,user_input)

# Condition while Cow != 4
while cow != 4:
    x=check()
    count  = count+1
    cow=x[0]
    bull=4-cow
    data.append(x[2])
    # print("---------------------")
    print("cow : {} | bull : {}".format(cow,bull))
    print("========================")
print("Guessed in {} attempt".format(count))
print("========================")
for i in data:
    print("history : {}".format(i))
