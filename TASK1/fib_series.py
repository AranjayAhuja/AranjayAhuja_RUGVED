from fibonnacci import fibo
series = []
n = int(input("Enter a number: "))
for i in range(n+1):
    series.append(str(fibo(i)))
fin_ser = ", ".join(series)
print(fin_ser)