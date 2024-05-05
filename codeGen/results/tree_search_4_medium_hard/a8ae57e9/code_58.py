import sys

n, k = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(i, k) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][max(0, j - 1)] + requests[i - 1][1] * min(k, requests[i - 1][0]))
print(f"{dp[n][k]} {requests.count(0)}")
for i in range(n):
    if requests[i][1] > dp[n][k]:
        print(f"Request {i + 1} cannot be seated.")
    else:
        for j in range(k, -1, -1):
            if dp[i][j] == dp[n][k]:
                print(f"Request {i + 1} seats at table {j}.")
