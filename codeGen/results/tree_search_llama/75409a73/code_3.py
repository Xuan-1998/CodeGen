import sys

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(calculate_factorial(n))
