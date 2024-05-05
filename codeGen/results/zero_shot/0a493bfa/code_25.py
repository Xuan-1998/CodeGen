import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    return n, m, a, b

n, m, a, b = read_input()

def f(s):
    p = min([i for i in range(2, int(s ** 0.5) + 1) if s % i == 0])
    return f(s // p) + s if p not in b else f(s // p) - s

max_beauty = float('-inf')

for i in range(n):
    for j in range(i + 1, n):
        gcd = abs(a[i] - a[j])
        while gcd > 1:
            if is_prime(gcd):
                gcd = gcd // min([i for i in range(2, int(gcd ** 0.5) + 1) if gcd % i == 0])
            else:
                break
        beauty = f(a[i] * a[j] // gcd)
        max_beauty = max(max_beauty, beauty)

print(max_beauty)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
