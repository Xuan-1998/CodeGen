import math

def prime_factors(n):
    i = 2
    factors = []
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
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        m = int(input())
        prime_factors_list = list(map(int, input().split()))
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        k = 1
        for p in prime_factors_list:
            k *= p
        labels = [0] * (n-1)
        for i, edge in enumerate(edges):
            u, v = edge
            labels[i] = min(u, v) + 1
        max_distribution_index = sum(sum(labels[:i+1]) for i in range(n-2))
        print(max_distribution_index % (10**9 + 7))

solve()
