R = []
d = 42.195
print("""Enter the distances covered by athlets in Marathon
(Kilometers) please
(press q to terminate):""")

#getting input from user
while True:
    distance = input()
    if (distance == "q"):
        break
    elif ((float(distance) >= d) or (float(distance) < 0)):
        pass
    else:
        R.append(float(distance))

#sort the R in descending order
R.sort(reverse=True)

#print the R excluding finishers
print("Highest Distance excluding Finishers:")
if (len(R)>3):
    print([R[i] for i in range(0,3)])
else:
    print(R)
