import sys

def prime_factors(k):
    i = 2
    factors = []
    while i * i <= k:
        if k % i:
            i += 1
        else:
            k //= i
            factors.append(i)
    if k > 1:
        factors.append(k)
    return factors

def solve():
    n = int(input())
    edges = list(map(int, input().split()))
    m = int(input())
    prime_factors_list = list(map(int, input().split()))
    
    memo = {}
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    def dfs(u, v):
        if u == v:
            return 0
        if (u, v) in memo:
            return memo[(u, v)]
        res = float('inf')
        for i in range(edges[u - 1], edges[v - 1] + 1):
            res = min(res, dfs(u, edges[i - 1]) + i)
        memo[(u, v)] = res
        return res

    total_sum = 0
    for i in range(1, n):
        total_sum += dfs(1, i)

    print((total_sum % (10**9 + 7)))

solve()
