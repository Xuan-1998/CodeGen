import sys
from collections import defaultdict

mod = 10**9 + 7

def prime_factors(k):
    i = 2
    factors = []
    while i * i <= k:
        if k % i:
            for j in range(2, int(k**0.5) + 1):
                if k % j == 0:
                    return [j]
        else:
            factors.append(i)
            k //= i
    if k > 1:
        factors.append(k)
    return factors

def dp(u, v, n, edges, primes):
    visited = [False] * (n + 1)
    parent = defaultdict(int)

    def dfs(node):
        visited[node] = True
        for neighbor in edges[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                dfs(neighbor)

    dfs(u)

    path_product = 1
    ones_in_path = 0

    while v != u:
        product = 1
        count_ones = 0
        while v != u:
            product *= primes[edges[v][0]]
            count_ones += 1
            v = parent[v]

        path_product *= product
        ones_in_path += count_ones

    return (path_product, ones_in_path)

n = int(input())
edges = [[] for _ in range(n + 1)]
primes = []
m = int(input())
for _ in range(m):
    p = int(input())
    primes.append(p)
k = 1
for prime in primes:
    k *= prime

max_distribution_index = 0

while n > 1:
    for i in range(1, n):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    path_products = []
    ones_in_paths = []

    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        product, ones = dp(u, v, n, edges, primes)
        path_products.append(product)
        ones_in_paths.append(ones)

    max_distribution_index += sum(path_product ** (n - 2) * ones_in_path for path_product, ones_in_path in zip(path_products, ones_in_paths))
    n -= 1

print(max_distribution_index % mod)
