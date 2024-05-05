import sys

n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    ci, pi = map(int, input().split())
    for j in range(1, min(i, k)+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + min(k, ci) * pi
max_earnings = max(max(row) for row in dp)
accepted_requests = sum(1 for i in range(n+1) for j in range(k+1) if dp[i][j] == max_earnings)
total_amount = sum(pi * min(k, ci) for i in range(n+1) for j in range(k+1) if dp[i][j] == max_earnings)
tables_to_use = [(i+1, j+1) for i in range(n+1) for j in range(k+1) if dp[i][j] == max_earnings]
print(accepted_requests)
print(total_amount)
for request, table in tables_to_use:
    print(request, table)
