import sys
from math import gcd

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        
        k = 1
        m = int(sys.stdin.readline())
        factors = list(map(int, sys.stdin.readline().split()))
        for p in factors:
            k *= p
        
        label = [0] * (n-1)
        for i in range(n-1):
            u, v = edges[i]
            if gcd(k, 2) == 2 and u < v:  # If k is even, make sure the first edge has a label of 1
                label[i] = 1
        
        total = sum((label[i] * (n-1-i)) for i in range(n-1))
        
        print(total % (10**9 + 7))

if __name__ == "__main__":
    solve()
