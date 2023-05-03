class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print('Empty')
        else:
            temp=self.head
            print(temp.data,"-->",end="")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end="")
            print()
    def search(self):
        x=int(input("enter element to be searched"))
        temp=self.head
        count=0
        flag=0
        while(temp!=self.tail):
            if x==temp.data:
                flag=1
                break
            else:
                temp=temp.next
                count+=1
        else:
           if x==temp.data:
              flag=1
        if flag==1:
              print("Element",x,"found at the position",count+1)
        else:
              print("Not found")





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
cll.display()
n2=Node(30)
cll.tail.next=n2
cll.tail=n2
cll.tail.next=cll.head
cll.display()
n2=Node(40)
cll.tail.next=n2
cll.tail=n2
cll.tail.next=cll.head
cll.display()
cll.search()