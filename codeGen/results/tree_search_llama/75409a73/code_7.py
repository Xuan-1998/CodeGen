def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(factorial(n))
