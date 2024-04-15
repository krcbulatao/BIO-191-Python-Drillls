first = int(input("Please enter an integer: "))
second = int(input("Please enter another integer: "))
third = int(input("Please enter a third integer: "))
odd = True

if first%2==1 or second%2==1 or third%2==1:
    odd = True
else:
    print ("None of the three numbers are odd.")

if odd:
    maxNum=first
    if second>maxNum:
        maxNum=second
    if third>maxNum:
        maxNum=third

print (maxNum, "is the greatest")


