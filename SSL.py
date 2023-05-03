class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def inbeg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def inen(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def inpos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
    def pri(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,end="--->")
                temp=temp.next
    def delb(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def dele(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delp(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp=None


llist=LinkedList()
    #llist.head
n=Node(10)
llist.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
llist.inbeg(5)
for i in range(10):

  llist.inbeg(i)
for i in range(10,29):
  llist.inen(i)
llist.inpos(4,25)
llist.delb()
llist.dele()
llist.delp(9)
llist.pri()