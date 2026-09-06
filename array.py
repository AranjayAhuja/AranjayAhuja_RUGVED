def first_repetition(arr):
    scanned =[]
    for num in arr:
        if num in scanned:
            return num
        else:
            scanned.append(num)
    return "No elements repeated"

n = int(input("Enter number of elements: "))
array = []
for i in range(n):
    x = int(input("Enter element: "))
    array.append(x)
print(first_repetition(array))