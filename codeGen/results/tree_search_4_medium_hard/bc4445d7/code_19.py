def solve(n, edges, m, prime_factors):
    memo = {}

    def dfs(i, k, l):
        if (i, k, l) in memo:
            return memo[(i, k, l)]

        res = 1e9
        for j in range(n):
            if j != i and edges[i][j] > 0:
                for p in prime_factors:
                    if k % p == 0:
                        new_k = k // p
                        new_l = l + (k % p == 1)
                        res = min(res, dfs(j, new_k, new_l) * edges[i][j])
        return res

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if edges[i][j] > 0:
                k = 1
                l = 0
                for p in prime_factors:
                    while k % p == 0:
                        k //= p
                        l += (k % p == 1)
                ans = max(ans, dfs(i, k, l) + dfs(j, k, l))
    return ans % (10**9+7)
