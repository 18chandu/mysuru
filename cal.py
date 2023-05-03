a=int(input("Enter 1st integer"))
b=int(input("Enter 2nd integer"))
opr=input("Enter the operation")


def switch(opr,a,b):
    if opr=='+':
        print("The addition is",a+b)
    elif opr=='-':
        print("The subtraction is",a-b)
    elif opr=='*':
        print("The multiplication is",a*b)
    elif opr=='/':
        print("The integer division is",a/b)
    else:
        print("The floor division is",a//b)


switch(opr,a,b)