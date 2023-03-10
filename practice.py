from cmath import pi
import math
print("Select one of the following :")
print(" 1) Square \n 2) Triangle ")
opt = int(input("Enter a number:" ))
if opt ==1:
    side = int(input("Enter length of a side: "))
    print(side**2)
elif opt ==2:
    base = int(input("Enter length of base: "))
    height = int(input("Enter length of height: "))
    print(1/2 * base * height)
else:
    print("error")