import sys

def vasya_moves():
    n = int(input())
    p = [0] + list(map(int, input().split()))
    dp = [[[-sys.maxsize for _ in range(3)] for _ in range(n+1)] for _ in range(3)]
    dp[0][1][0] = 0
    for i in range(2, n+2):
        if i % 2 == 0:
            dp[i][0][0] = min(dp[p[i-1]][2][0] + 1, dp[i-1][0][0] + 1)
        else:
            dp[i][1][0] = min(dp[p[i-1]][1][0] + 1, dp[i-1][1][0] + 1)
    return (dp[n+1][2][0]) % 1000000007

print(vasya_moves())
