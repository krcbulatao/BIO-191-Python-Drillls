def Prime (n):
    if n==1 or n==0:
        return False
    
    for i in range (2,n):
        if (n%i==0):
            return False
    return True

N=int(input("Enter N: "))

for i in range (1,N+1):
    if (Prime(i)):
        print (i, end=" ")

#Reference: Program to print prime numbers from 1 to N. [Online forum post]. (2024, February 28). geeksforgeeks.org. Retrieved April 14, 2024, from https://www.geeksforgeeks.org/program-to-print-first-n-prime-numbers/