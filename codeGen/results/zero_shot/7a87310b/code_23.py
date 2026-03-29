import sys

def generate_matrices(n):
    count = 0
    for a in range(1, n//2 + 1):
        b = n - a
        d = (a * d - c * b) // ((a - c) ** 2)
        if d > 0 and gcd(a * d - c * b, (a - c) ** 2) == 1:
            count += 1
    return count

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(generate_matrices(n))
