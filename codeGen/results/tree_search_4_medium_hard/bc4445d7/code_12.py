from collections import defaultdict

def solve(n, edges, k):
    memo = defaultdict(int)
    def dfs(u, parent=None):
        if u == -1:
            return 1
        if (u, parent) in memo:
            return memo[(u, parent)]
        res = 0
        for v in edges[u]:
            if v != parent:
                res += dfs(v, u)
        memo[(u, parent)] = res
        return res

    def has_product(k):
        primes = [2, 3, 5, 7, 11, 13]
        for p in primes:
            while k % p == 0:
                k //= p
        return k != 1

    def max_distribution_index():
        res = 0
        for u in range(n):
            for v in range(u+1, n):
                if has_product(k // dfs(v, u)):
                    res += dfs(v, u)
        return res % (10**9 + 7)

    return str(max_distribution_index())
