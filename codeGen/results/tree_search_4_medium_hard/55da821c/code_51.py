import heapq

n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][j] = 0 for j in range(m + 1)

pq = []
for i in range(1, n + 1):
    x, s = map(int, input().split())
    heapq.heappush(pq, (x, s))

for i in range(1, n + 1):
    min_replanted = float('inf')
    while pq:
        x, s = heapq.heappop(pq)
        for j in range(1, m + 1):
            if dp[i-1][j-1] > 0 and s == j:  # reuse replantings
                replanted = dp[i-1][j-1]
            else:
                replanted = sum(dp[i-1][k] for k in range(j)) + 1
            min_replanted = min(min_replanted, replanted)
        dp[i][s] = min_replanted

print(dp[n][m])
