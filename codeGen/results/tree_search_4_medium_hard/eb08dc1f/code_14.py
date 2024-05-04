import sys

def solve(n):
    MOD = 998244353
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][1] = int(10**(n-1)) % MOD

    for i in range(2, n+1):
        for k in range(i+1):
            if k == 0:
                continue
            for j in range(i-k+1):
                for l in range(1, min(k+1, i-j+2)):
                    dp[i][k] += dp[j][l] * (10**(i-j)-1) % MOD
    answer = sum(dp[i][k] for k in range(n+1)) % MOD

    return str(answer)

n = int(input())
print(solve(n))
