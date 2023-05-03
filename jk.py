print("O for false,1 for true")
pr=int(input("Preset?"))
cl=int(input("Clear input?"))
q=int(input("Enter the present state of the flip flop"))
if pr==0 and cl==1:
    print(f"Next state is equal to {True}")
elif pr==1 and cl==0:
    print("Next state is equal to {}".format(False))
elif pr==0 and cl==0:
    print("Invalid")
else:
    clock=int(input("Enter the clock input"))
    if clock==1:
        j=int(input("Enter J"))
        k=int(input("Enter k"))
        if j==0 and k==0:
            print("next state is equal to present state {}".format(bool(q)))
        elif j == 0 and k == 1:
            print(f"Next state is equal to {False}")
        elif j == 1 and k == 0:
            print(f"Next state is equal to {True}")
        else:
            print(f"Next state is equal to {not (q)}")
    else:
       print(f"Next state is equal to present state {bool(q)}")



