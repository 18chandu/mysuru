for i in range(1,5):
    for j in range(i):
        if i%j==0:
            break
        else:
            print(i,end="")