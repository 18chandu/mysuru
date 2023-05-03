anode_v=int(input("Anode voltage?"))
cathode_v=int(input("Cathode voltage?"))
print("Forward biased") if anode_v>cathode_v else print("Reverse biased")
