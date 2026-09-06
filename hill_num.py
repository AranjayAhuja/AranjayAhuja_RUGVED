def hill_num(num):
    x = str(num)
    n = len(x)
    if n<3:
        return False
    i = 0
    while i<n-1 and x[i]<x[i+1]:
        i+=1
    if i == 0 or i ==n-1:
        return False
    while i<n-1 and x[i]>x[i+1]:
        i+=1
    if i == n-1:
        return True

inp = int(input("Enter number: "))
if hill_num(inp):
    print("Its a hill number")
else:
    print("Not a hill number")










