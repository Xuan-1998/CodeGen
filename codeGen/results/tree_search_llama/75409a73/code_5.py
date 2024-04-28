import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > sys.maxsize:  # Handle overflow errors
        print("Factorial exceeds maximum integer value. Using modulo operation.")
        result = pow(n, n) % (2**31 - 1)
    else:
        result = n * factorial(n-1)
    return result

t = int(input())  # Read the number of test cases
for _ in range(t):
    n = int(input())  # Read the integer n
    print(factorial(n))
