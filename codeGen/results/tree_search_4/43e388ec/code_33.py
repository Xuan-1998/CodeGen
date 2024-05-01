def solve(a, b):
    MOD = 10**9 + 7
    dp = [[0] * (b+1) for _ in range(len(bin(a)) - 2)]

    for i in range(1, len(bin(a)) - 1):
        for j in range(b+1):
            if a[i-1] == '1':
                dp[i][j] = dp[i-1][(j+1)%b]
            else:
                dp[i][j] = dp[i-1][(j+1)%b] + (a[i-1]^b[j])

    return sum(dp[-1]) % MOD

# Read input from stdin
a, b = map(int, input().split())
print(solve(a, b))
