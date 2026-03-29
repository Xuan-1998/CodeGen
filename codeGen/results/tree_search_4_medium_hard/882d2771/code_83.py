def solve(t, l, r):
    MOD = 10**9 + 7

    # Precompute values for f(i) for i = 1, 2, ..., r
    f = [0] * (r + 1)
    f[1] = 1
    for i in range(2, r + 1):
        f[i] = min(f[i - 1], i)

    # Initialize memoization table
    memo = [[[-1, float('inf')] for _ in range(l + 1)] for _ in range(r + 1)]

    def dp(n, k, g):
        if n == 1:
            return 0

        if (n, k, g) in memo[k][g]:
            return memo[k][g][(n, k, g)]

        result = float('inf')
        for j in range(k, 0, -1):
            result = min(result, dp(n - j, k, g) + f[j] + j)

        memo[k][g][(n, k, g)] = result
        return result

    # Calculate the value of the expression
    total = 0
    for i in range(t):
        total += (i % MOD) * f[l]
    for i in range(l, r + 1):
        total -= (l % MOD) * f[i]

    return total % MOD


t, l, r = map(int, input().split())
print(solve(t, l, r))
