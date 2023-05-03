


def push():
    n=int(input("Enter the element"))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,"is inserted into stack")
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("deleted")
        del stack[0]
def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        for i in stack:
            print(i)




stack=list()
while(1):
    print("Enter")
    str=input()
    if str=='1':
        print("PUSH")
        push()
    elif str=='2':
        print("POP")
        pop()
    elif str=='3':
        print("Display")
        display()

    else:
        print("Exit")
        break



