def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(calculate_factorial(n))
