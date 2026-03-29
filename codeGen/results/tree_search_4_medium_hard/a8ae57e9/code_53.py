from collections import defaultdict

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
requests = []
for i in range(n):
    ci, ri = map(int, input().split())
    requests.append((ci, ri))

for i in range(1, n+1):
    for j in range(1, min(i, k)+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + sum(min(ci, k) for ci, _ in requests[:i])

accepted_requests = 0
total_money = 0
for i in range(n, 0, -1):
    for j in range(k, 0, -1):
        if dp[i][j] > dp[i-1][j]:
            accepted_requests += 1
            total_money += sum(min(ci, k) for ci, _ in requests[:i])
            print(i, j)

print(accepted_requests)
print(total_money)
