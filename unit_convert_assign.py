#!/usr/bin/env python3
import sys

#====================== Print Menu Of Unit Conversion ==========================
def menu():
    print("======== Unit Converter ========")
    print(">> Press 1 : Binary to Decimal  ")
    print(">> Press 2 : Decimal to Hexadecimal")
    print(">> Press 3 : Decimal to Octadecimal")
    print(">> Press 4 : Exit the Program")
    print("=================================")
    user_input = input(">> Choice : ")
    if user_input == '1':
        binary()
    elif user_input == '2':
        hex()
    elif user_input == '3':
        octal()
    else:
        sys.exit()
#===============================================================================

#========================== Define Binary function =============================
def binary():
    dec_data=[1]
    a=b=1
    print("======= Binary to Decimal =======")
    binary = input('>> Enter Binary number : ')
    length=len(binary)-1
    # Generating decimal value for binary
    while length > 0:
        a=b
        b=data=a+b
        length=length-1
        dec_data.append(data)
    sum = 0
    for i in range(1,len(binary)+1):
        if binary[-i] == '0':
            continue
        else:
            sum = sum + dec_data[i-1]
    print("=================================")
    print("Binary : {} -> Decimal : {}\n".format(binary,sum))
    mood=input("=================================\n>> Press 1 : Try Again\n>> Press 2 : Menu\n>> Press 3 : Exit the Program\n=================================\nChoice : ")
    if(mood=='1'):
        octal()
    elif(mood=='2'):
        menu()
    else:
        sys.exit()

#===============================================================================

#============================ Define hex function ==============================
def hex():
    print("======= Decimal to Hexadecimal =======")
    x=int(input(">> Enter Decimal number : "))
    new_data=[]
    hex_data=[]
    y=int(x/16)
    hex_data.append(int(x%16))
    while y != 0:
        hex_data.append(int(y%16))
        y=int(y/16)
    for i in range(1,len(hex_data)+1):
        if hex_data[-i]<=9:
            new_data.append(str(hex_data[-i]))
        elif hex_data[-i]==10:
            new_data.append('A')
        elif hex_data[-i]==11:
            new_data.append('B')
        elif hex_data[-i]==12:
            new_data.append('C')
        elif hex_data[-i]==13:
            new_data.append('D')
        elif hex_data[-i]==14:
            new_data.append('E')
        elif hex_data[-i]==15:
            new_data.append('F')
    separ=''
    result=separ.join(new_data)
    print("=================================")
    print("Decimal : {} -> Hexadecimal : {}\n".format(x,result))
    mood=input("=================================\n>> Press 1 : Try Again\n>> Press 2 : Menu\n>> Press 3 : Exit the Program\n=================================\nChoice : ")
    if(mood=='1'):
        hex()
    elif(mood=='2'):
        menu()
    else:
        sys.exit()

#===============================================================================

#========================== Define octal function ==============================
def octal():
    print("======= Decimal to Octadecimal =======")
    x=int(input(">> Enter Decimal number : "))
    new_data=[]
    hex_data=[]
    y=int(x/8)
    oct_data.append(int(x%8))
    while y != 0:
        oct_data.append(int(y%8))
        y=int(y/8)
    for i in range(1,len(oct_data)+1):
        if oct_data[-i]<=7:
            new_data.append(str(oct_data[-i]))
    separ=''
    result=separ.join(new_data)
    print("=================================")
    print("Decimal : {} -> Octal : {}\n".format(x,result))
    mood=input("=================================\n>> Press 1 : Try Again\n>> Press 2 : Menu\n>> Press 3 : Exit the Program\n=================================\nChoice : ")
    if(mood=='1'):
        octal()
    elif(mood=='2'):
        menu()
    else:
        sys.exit()

#===============================================================================

menu()
