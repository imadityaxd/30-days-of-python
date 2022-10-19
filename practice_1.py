#
#num = []
#for i in range(2):
#    #getting input in array
 #   num.append(int(input("Enter a number: ")))

#if num[0]>num[1]:
#    print(num[1], num[0])
#else: 
#    print(num[0],num[1])

age = int(input("Enter your age: "))
if age>=18:
    print ("You can vote")
elif age==17:
    print("You can learn to drive.")
elif age==16:
    print("You can buy a lottery ticket.")
elif age<16:
    print("You can go trick-treat.")
    
