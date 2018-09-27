#!/usr/bin/env python3

user_list=[1,2,[3,4,5,[6,7],9],5,1]
print("original list")
print(user_list)
new_list=[]
# Define function
def check(user_list):
    for i in user_list:
        if type(i)!=type(user_list):
            new_list.append(i)
        else:
            check(i)
check(user_list)
print("\nNew list")
print(new_list)
