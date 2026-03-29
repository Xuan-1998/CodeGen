import sys

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    pi, ci = map(int, input().split())
    for j in range(1, min(i, k) + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1] + pi * min(k, ci))

print(f"{dp[n][k]}")  # Output: total amount of money earned

# If we want to output the accepted requests and table assignments:
m = sum(1 for i in range(n) if dp[i][k] != dp[i+1][k])
print(m)  # Output: number of accepted requests
for i in range(n):
    if dp[i][k] > dp[i+1][k]:
        print(f"Request {i+1}: Table {k}")
