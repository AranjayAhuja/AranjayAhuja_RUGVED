def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
if __name__ == "__main__":
    x = int(input("Enter a number: "))
    print(str(fibo(x)) + " is the fibonacci number")