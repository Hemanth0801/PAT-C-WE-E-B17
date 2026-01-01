num  = lambda n: n if n <= 1 else num(n - 1)+num(n - 2)
n = int(input("Enter a number: "))
fibnocci_series = [num(i)  for i in range(n)]
print(fibnocci_series)
