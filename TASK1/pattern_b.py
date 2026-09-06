def butterfly(n):
    for i in range(1,n):
        print("*"*i,end="")
        print(" "*((2*(n-i))-1),end="")
        print("*"*i)
    print("*"*((2*(n-1))+1))
    for i in range(n-1,0,-1):
        print("*"*i, end="")
        print(" "*((2*(n-i))-1),end="")
        print("*"*i)


n = int(input("Enter N:"))
butterfly(n)
