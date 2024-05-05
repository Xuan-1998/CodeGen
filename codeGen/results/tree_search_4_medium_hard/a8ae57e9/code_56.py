import sys

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

pi, ci = [], []
for i in range(n):
    pi.append(int(input()))
    ci.append(min(k, int(input())))

for i in range(1, n + 1):
    for j in range(min(i, k) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + min(pi[i - 1] * ci[i - 1], ci[i - 1] * min(k, ci[i - 1]))

accepted_requests, total_money_earned = 0, 0
for i in range(n, 0, -1):
    for j in range(min(i, k) + 1):
        if dp[i][j] > total_money_earned:
            accepted_requests = i
            total_money_earned = dp[i][j]

print(accepted_requests, total_money_earned)

for i in range(accepted_requests, 0, -1):
    for j in range(min(i, k) + 1):
        if dp[i][j] == total_money_earned:
            print(i, j)
