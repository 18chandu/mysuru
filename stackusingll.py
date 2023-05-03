class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def push(self):
        x=int(input("element"))
        new=Node(x)
        if self.top is None:
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top is None:
            print("Empty")
        elif self.top.next is None:
            print("Popped element is",self.top.data)
            print("--------------")
            self.top=None
        else:
            temp=self.top
            print("Popped element is",self.top.data)
            print("----------------")
            self.top=temp.next
            temp=None
    def display(self):
        if self.top is None:
            print("Elements are")
            print("--------")
        else:
            print("Elemnts r")
            temp=self.top
            while temp:
                 print(temp.data)
                 temp=temp.next
            print("Top is",self.top.data)
        print("-------")



s=Stack()
while(1):
    n=input("Enter the option \n 1.Push 2.Pop 3.Display")
    if n=='1':
        print("Push operation")
        print("--------")
        s.push()

    elif n=='2':
        print("Pop operation")
        print("--------")
        s.pop()
    elif n=='3':
        print("Display")
        print("---------")
        s.display()
    else:
        break




