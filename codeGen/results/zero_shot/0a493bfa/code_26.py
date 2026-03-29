import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Read input from stdin
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Initialize maximum beauty to 0
max_beauty = 0

code...
