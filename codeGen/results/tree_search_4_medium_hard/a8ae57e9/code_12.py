import sys

n, k, max_capacity = map(int, input().split())
dp = [[[0] * (k+1) for _ in range(max_capacity+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        for cap in range(max_capacity+1):
            if i == 0 or j == 0:
                dp[i][j][cap] = 0
            elif cap >= requests[i-1][0]:
                accept = dp[i-1][max(0, j-requests[i-1][0])][cap - requests[i-1][0]] + requests[i-1][1]
                decline = dp[i-1][j][cap]
                dp[i][j][cap] = max(accept, decline)
            else:
                dp[i][j][cap] = dp[i-1][j][cap]

max_earnings = 0
for i in range(k+1):
    for cap in range(max_capacity+1):
        if dp[n][i][cap] > max_earnings:
            max_earnings = dp[n][i][cap]
            accepted_requests = n - (k-i)
            remaining_tables = i

print(accepted_requests, max_earnings)

for _ in range(accepted_requests):
    for cap in range(max_capacity+1):
        if dp[accepted_requests-1][remaining_tables-1][cap] == dp[n][i][cap]:
            print(_+1, cap)
            break
