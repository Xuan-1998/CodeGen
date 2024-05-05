===BEGIN CODE===
from math import gcd
from functools import lru_cache

def solve():
    n = int(input())
    parent = [i for i in range(n)]
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        if parent[v] != v:
            parent[u] = v
        else:
            parent[v] = u
        edges.append((u, v))

    m, k = map(int, input().split())
    primes = list(map(int, input().split()))

    @lru_cache(None)
    def dfs(node):
        if parent[node] == node:
            return 1, 0

        child_sum, _ = dfs(parent[node])
        child_product = int(gcd(child_sum, k//child_sum) if child_sum else 1)

        left_sum, right_sum = 1, 1
        for edge in edges:
            u, v = edge
            if u == node:
                v = parent[node]
            elif v == node:
                v = parent[node]

            if u == v:
                continue

            if u != node and v != node:
                left_sum *= int(gcd(left_sum, 1) if left_sum % (v-1) else 1)
            elif u == node or v == node:
                right_sum *= int(gcd(right_sum, 1) if right_sum % ((n-1)-node) else 1)

        return child_sum * child_product * left_sum * right_sum, child_sum + left_sum + right_sum

    max_dist_index = 0
    for i in range(n):
        _, dist = dfs(i)
        max_dist_index = max(max_dist_index, dist)

    print(max_dist_index % (10**9+7))

solve()
