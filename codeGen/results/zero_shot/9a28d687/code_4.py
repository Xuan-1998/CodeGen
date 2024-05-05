import sys

n = int(input())
costs = [int(input()) for _ in range(n)]
strings = [input() for _ in range(n)]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = sys.maxsize
    if strings[i-1] < strings[0]:
        dp[i] = costs[i-1]
    else:
        for j in range(i - 1, -1, -1):
            if strings[j] >= strings[i-1]:
                dp[i] = min(dp[i], dp[j] + costs[i-1])
                break

print(-1) if dp[n] == sys.maxsize else print(dp[n])
