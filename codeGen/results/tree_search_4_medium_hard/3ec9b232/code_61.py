import sys

def solve(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if m[i - 1] == m[i - 2]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = sum(dp[j] for j in range(i)) % (10**9 + 7)
    return dp[n]

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
print(solve(n, m))
