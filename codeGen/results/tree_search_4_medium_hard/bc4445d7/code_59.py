import heapq
def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = list(map(int, input().split()))
        m = int(input())
        primes = list(map(int, input().split()))
        k = 1
        for p in primes:
            k *= p

        dp = [[0] * (n + 5) for _ in range(n + 5)]
        memo = {}

        def dfs(i):
            if i == n - 1: return 1
            if dp[i][i]: return dp[i][i]
            parent = [j for j in range(n) if edges[j] == i][0]
            p = 1
            for prime in primes:
                while k % prime == 0 and p < prime:
                    p *= prime
                    k //= prime
            for child in range(parent + 1, n):
                if edges[child] == i: p *= (child - parent)
            dp[i][i] = p
            return dfs(parent) * p

        print(dfs(0))
