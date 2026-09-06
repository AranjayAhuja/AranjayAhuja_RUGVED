def diamond(n):
    for i in range (1,n+1):
        print(" "*(n-i), end="")
        print("* " *i)
    for i in range(n,0,-1):
        print(" "*(n-i), end="")
        print("* " *i)

n = int(input("Input: "))
print("Output:")
diamond(n)