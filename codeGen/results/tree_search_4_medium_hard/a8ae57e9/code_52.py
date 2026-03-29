import heapq

n, k = map(int, input().split())  # number of requests, number of tables
requests = [[*map(int, input().split()), int(input())] for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]
pq = []

for i in range(1, n + 1):
    for j in range(1, k + 1):
        ci, pi = requests[i-1]
        if j >= ci:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + pi * min(k, ci)
        else:
            dp[i][j] = dp[i-1][j]
        if i > 0 and j > 0:
            heapq.heappush(pq, (-pi, i))

total_earned = 0
accepted_requests = 0

while pq:
    _, request_idx = heapq.heappop(pq)
    ci, pi = requests[request_idx]
    if ci <= k:
        total_earned += pi
        accepted_requests += 1
    print(f"{request_idx} {k - ci + 1}")

print(accepted_requests, total_earned)
