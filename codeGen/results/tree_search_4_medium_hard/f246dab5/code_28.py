import sys

n = int(input())
dp = [0] * (n + 1)
t = [0] * n

for i in range(n):
    t[i] = int(input())

min_cost = 0
last_used_ticket = 0

for i in range(1, n + 1):
    if t[i - 1] <= 60:  # one trip ticket
        min_cost += 20
    elif t[i - 1] <= 90 * 60:  # 90 minutes ticket
        if last_used_ticket == 0:
            min_cost += 50 * (t[i - 1] // 60)
        else:
            min_cost += 50
    else:  # one day ticket
        if last_used_ticket == 0:
            min_cost += 120
        else:
            min_cost += 20

    dp[i] = min_cost

print(min_cost)

