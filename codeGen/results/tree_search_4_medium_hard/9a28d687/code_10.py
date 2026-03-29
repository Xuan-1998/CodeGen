from sys import stdin
n = int(stdin.readline())
costs = list(map(int, stdin.readline().split()))
strings = [stdin.readline() for _ in range(n)]

dp = [[0, float('inf')] for _ in range(n+1)]
for i in range(1, n+1):
    if strings[i-1] < strings[i]:
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + costs[i]
    else:
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + costs[i]

print(min(dp[n]))
