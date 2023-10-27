# n = int(input("Enter number:"))
# if n % 2 == 0:
#     print("your numbe is even")
# else:
#     print("your number is odd")

n = int(input("Enter items:"))
newlist = []
for i in range(n):
    i = int(input("Enter {} digits:".format(i)))
    newlist.append(i)

evenlist = []
oddlist = []
for i in newlist:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Your even number is :",evenlist)
print("Your odd number is :",oddlist)