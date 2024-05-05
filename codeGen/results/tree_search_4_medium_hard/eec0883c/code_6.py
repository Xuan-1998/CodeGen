from collections import deque

def max_gas(n, w, roads):
    dp = [[0] * (w[i] + 1) for i in range(n)]
    dp[0][w[0]] = w[0]

    for c, d, cost in roads:
        for j in range(w[d] - cost, -1, -1):
            dp[c][j] = max(dp[c][j], min(w[c], j))
        for j in range(w[d] + 1):
            if j <= w[d]:
                dp[c][j] = max(dp[c][j], dp[d][min(j, w[d] - cost)])

    return max(dp[-1])

n = int(input())
w = list(map(int, input().split()))
roads = []
for _ in range(n-1):
    c, d, cost = map(int, input().split())
    roads.append((c, d, cost))

print(max_gas(n, w, roads))
