n, k = map(int, input().split())
dp = [[0]*k for _ in range(n)]
min_tables = [[float('inf')] * k for _ in range(n)]

for i in range(n):
    ci, pi = map(int, input().split())
    for j in range(min(k, ci), -1, -1):
        dp[i][j] = max(dp[i-1][k] + pi for k in range(1, min(j+1, ci)) if ci <= k)
        min_tables[i][j] = min(min_tables[i-1][k] + (1 if ci > k else 0) for k in range(1, j+1))

max_earnings = max(dp[-1])
min_tables_required = min_tables[-1].index(max_earnings)

print(f"{n} {max_earnings}")
for i in range(n):
    print(i, min_tables_required)
