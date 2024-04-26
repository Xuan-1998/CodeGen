def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())  # Read t from stdin

for _ in range(t):
    n = int(input())  # Read n from stdin
    print(factorial(n))  # Calculate and print the factorial of n
