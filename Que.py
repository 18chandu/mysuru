queue=list()


def enqueue():
   n=int(input("Element"))
   queue.append(n)
   print()

def dequeue():
    if len(queue)==0:
        print("Queue is empty")
        print("----------")
    else:
        print(queue[0], "is the deleted element")
        del queue[0]
        print("-----------")
def display():
    if len(queue)==0:
        print("Que is empty")
    else:
        print("Elements are")
        for x in queue:
            print(x,end=" ")
        print("Front of the is",queue[0])
        print("Rear of the is",queue[-1])


while(1):
    print("1.Enque 2.Deque 3.Display 4.Exit")
    op=input()
    if op=='1':
        print("Enqueue")
        enqueue()
    elif op=='2':
        print("Dequeue")
        dequeue()
    elif op=='3':
        print("Display")
        display()
    else:
        break
