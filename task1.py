def sum(x,y):
    return x+y
def dif(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
z=input("enter the opeation you want to prform  +,-,*,/:")
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))

if z=="+":
    print('the sum is:',sum(x,y))
elif z=="-":
     print('the difference is:',dif(x,y))
elif z=="*":
    print('the product is:',mul(x,y))
elif z=="/":
     print('the quotient:',div(x,y))
else:
    print("invalid operation")
