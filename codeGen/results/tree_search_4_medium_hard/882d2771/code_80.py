import sys

def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [[0] * (t+1) for _ in range(r-l+2)]

    for i in range(1, t+1):
        if i == 1:
            dp[0][i] = min(l+r-1, l*r//2)
        else:
            for j in range(min(i, r-l+1), -1, -1):
                dp[j][i] = min(dp[j][i], dp[j-1][i-1] + (l+j)*(r-j)//2)

    return sum((t-i)*dp[0][i] for i in range(1, t+1)) % MOD

t, l, r = map(int, input().split())
print(solve(t, l, r))
