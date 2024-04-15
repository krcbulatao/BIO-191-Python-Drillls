N = int (input("Enter N: "))
print (N)

if N%2==1 and N>0: 
    for i in range(N):
        for j in range (N):
            if j == i :
                print("*", end="")
            elif i == N-1 :
                print("*", end="")
            elif j == 0 :
                print("*", end="")
        print("")
