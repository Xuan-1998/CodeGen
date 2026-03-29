import sys

def solve():
    n = int(sys.stdin.readline().strip())
    m = list(map(int, sys.stdin.readline().strip().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            if m[j - 1] <= i:
                dp[i][j] = (dp[i - 1][min(j - 1, i)] + dp[i - 1][max(0, j - 2)]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i - 1][j]
    
    return sum(dp[n]) % (10**9 + 7)

print(solve())
