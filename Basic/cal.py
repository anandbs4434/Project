import os

while True:
    os.system('cls')
    print("Calculator")
    print('1. ➕')
    print('2. ➖')
    print('3. ✖️')
    print('4. Exit')
    ch= input('Select a option  ')
    if ch=='1':
        a=int(input("Enter the number "))
        b=int(input("Enter the number "))
        print(f'{a} + {b} = {a+b}')
    elif ch=='2':
        a=int(input("Enter the number "))
        b=int(input("Enter the number "))
        print(f'{a} - {b} = {a-b}')
    elif ch=='3':
        a=int(input("Enter the number "))
        b=int(input("Enter the number "))
        print(f'{a} * 1{b} = {a*b}')
    elif ch=='4':
        print("☠️ ☠️ ☠️ ☠️")
        break
    else:
        print('Invalid input')
    input('continue')
