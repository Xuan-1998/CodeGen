import sys

n = int(input())
tickets = [[0, 20], [89, 50], [1439, 120]]
dp = [float('inf')] * (n + 1)

for i in range(n):
    for j in range(len(tickets)):
        if tickets[j][0] <= i:
            dp[i] = min(dp[i], dp[max(0, i - tickets[j][0]) - 1] + tickets[j][1])
        else:
            dp[i] = min(dp[i], dp[i - 1] + tickets[j][1])

print(*dp[:-1], sep='\n')
