from math import gcd

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def min_prime_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_f(a):
    beauty = 0
    for i in range(len(a)):
        p = min_prime_divisor(a[i])
        if p not in b:  # Good prime
            beauty += a[i]
        else:  # Bad prime
            beauty -= a[i]
    return beauty

def calculate_beauty(a, b):
    beauty = 0
    for i in range(len(a)):
        new_a = [gcd(x, a[:i] + a[i+1:]) for x in a]
        beauty = calculate_f(new_a)
    return beauty

print(calculate_beauty(a, b))
