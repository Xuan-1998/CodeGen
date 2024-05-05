import sys

# Read input
n, k = map(int, input().split())
p = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

# Initialize dp table
dp = [[0] * (k + 1) for _ in range(n + 1)]

# Fill dp table using bottom-up dynamic programming
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if p[i] <= c[j]:
            dp[i][j] = max(dp[i - 1][k - 1] + p[i] * c[j], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

# Find maximum amount of money earned and corresponding requests
max_earnings = max(dp[n])
accepted_requests = []
tables_used = []

for i in range(n, 0, -1):
    if dp[i][k] > dp[i][k - 1]:
        accepted_requests.append(i)
        tables_used.append(k)

# Print output
print(len(accepted_requests), max_earnings, sep='\n')
for request, table in zip(accepted_requests, tables_used):
    print(request, table)
