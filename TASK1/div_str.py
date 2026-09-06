inp = input("Enter the string")
n = int(input("Enter size of a part"))
length = len(inp)
if n<= 0 or length%n!=0:
    print("Division not possible")
else:
    part1 = inp[0:n]
    tot_parts = length // n
    if part1*tot_parts == inp:
        for i in range(0,tot_parts):
            print("'" + part1 + "' " ,end=" ")
