class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None


    def display(self):
        if self.head is None:
            print("Empty CLL")
        else:
            temp=self.head
            print(temp.data,"-->",end="")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end="")
            print(temp.next.data)
    def addb(self,x):
        new = Node(x)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            new.next=self.head
            self.tail.next=new
            self.head=new
    def adde(self,x):
        n=Node(x)
        if self.head is None:
            self.head=n
            self.tail=n
            self.tail.next=self.head
        else:
            self.tail.next=n
            self.tail=n
            self.tail.next=self.head
    def addp(self,x,pos):
        n=Node(x)
        if self.head is None:
            self.head = n
            self.tail = n
            self.tail.next = self.head
        else:
            if pos==1:
                 cll.addb(x)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                n.next=temp.next
                temp.next=n
    def delbe(self):
        if self.head is None:
            print('Empty in CCL')
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp = self.head
                self.head = temp.next
                temp = None
                self.tail.next =self.head


    def dele(self):
        if self.head is None:
            print('Empty in CCL')
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                while(temp.next != self.tail):
                 temp=temp.next
                self.tail=None
                self.tail=temp
                temp.next=self.head

    def pos(self,pos):
        if self.head is None:
            print('Empty in CCL')
        elif pos==1:
            cll.delbe()
        else:
            temp1=self.head
            temp2=self.head.next
            for i in range(1,pos-1):

                temp1=temp1.next
                temp2=temp2.next
            temp1.next=temp2.next
            if temp2==self.tail:
                self.tail=temp1
            temp2=None


cll=CLL()
n1=Node(10)
cll.head=n1
cll.tail=n1
cll.tail.next=cll.head
print("After 1st node")
cll.display()
n2=Node(20)
cll.tail.next=n2
cll.tail=n2
cll.tail.next=cll.head
print("After 2nd node")
cll.addb(45)
cll.display()
cll.addb(100)
cll.adde(56)
cll.adde(34)
cll.addp(35,2)
cll.display()
cll.delbe()
cll.display()
cll.delbe()
cll.display()
cll.dele()
cll.display()
cll.pos(4)
cll.display()
cll.pos(2)
cll.display()