print("you have 4 options")
print("Addition- 1")
print("subtraction- 2")
print("multiplication- 3")
print("divisionn-4")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

def calculator():
    s=True
    a=int(input('enter the first number '))
    while s :
        b = int(input('enter the second number '))  
        choice = int(input("enter your choice "))
        if choice == 1:
            a = add(a,b)
            print(a)
        elif choice == 2:
            a = sub(a,b)
            print(a)
        elif choice == 3:
            a = mul(a,b)
            print(a)
        elif choice == 4:
            if b==0:
                print("divid by zero not possible")
                b = int(input('enter the second number '))
            a = div(a,b)
            print(a)
        w = input("do you want to Continue / Restart / Stop c/r/s ").lower()
        if w == 'c':
            continue
        elif w == 'r':
            calculator()
        else:
            s = False
calculator()
        
        




