import sys

def solve(n, s):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    max_or = 0

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            or_val = int(s[i - 1:j], 2)
            for k in range(i):
                dp[k][j] = max(dp[k][j], or_val | int(s[k:i], 2))
            max_or = max(max_or, dp[0][j])

    return bin(max_or)[2:]

n = int(input())
s = input().strip()
print(solve(n, s))
