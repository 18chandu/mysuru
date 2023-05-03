class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DDL:
    def __init__(self):
        self.head=None
    def beg(self,data):
        nb=Node(data)


    def pri(self):
        if self.head is None:
            print("Empty")

        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
    def inb(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def ine(self,data):
        temp=self.head
        n=Node(data)
        while temp.next:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def inp(self,data,pos):
        temp=self.head
        n=Node(data)
        for i in range(0,pos-1):
            temp=temp.next

        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def deld(self,data):
        temp=self.head.next
        befor=self.head

        while temp.next:
           temp=temp.next
           befor=befor.next
        befor.next=None
        temp.prev= None
    def delb(self,data):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    def delp(self,pos):
        temp=self.head.next
        befor=self.head

        for i in range(0,pos-1):
            temp=temp.next
            befor=befor.next

        temp.prev=None
        befor.next=temp.next
        temp.next.prev=befor
        temp.next=None
l=DDL()

n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n1.prev=n
n2=Node(30)
n1.next=n2
n2.prev=n1
l.inb(20)
l.inb(7)
l.ine(3)
l.inp(18,3)
l.inp(19,3)

l.deld(3)
l.delb(7)
l.delp(3)
l.pri()