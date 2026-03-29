import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[0] * (len(max(strings)) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, len(max(strings)) + 1):
        dp[i][j] = sys.maxsize
        for k in range(i):
            if strings[k].endswith(strings[i-1][:j]):
                cost = costs[i - 1]
                if not strings[k]:
                    cost += costs[j - 1]
                dp[i][j] = min(dp[i][j], dp[k][j - j] + cost)

if dp[n][len(max(strings))] == sys.maxsize:
    print(-1)
else:
    print(dp[n][len(max(strings))])
