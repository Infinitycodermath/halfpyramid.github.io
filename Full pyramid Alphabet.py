n=int(input("Enter n:"))
alph=65
for i in range (1,n+1):#printing rows
    #prnting space
    print(" "*(n-i),end=" ")
    for j in range (1,i+2):
        print(chr(alph),end=" ")
        alph+=1
    alph=65
    print()

