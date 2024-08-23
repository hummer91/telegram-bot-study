n = int(input("Enter a number: "))

a, b = 0, 1
for _ in range(n):
    a , b = b, a+b
    print(a, end=" ")