import sys

n = int(input())
dp = [[[float('inf')] * (max(120, 50) + 1) for _ in range(max(10**9, n - 1) + 1)] for _ in range(3)]

dp[0][0][0] = 20
for i in range(1, n):
    minutes_left = min((i - 1), (10**9 - i) // 90 * 90)
    dp[2][minutes_left][0] = 120

for i in range(n):
    time_left = i + 1
    for cost_so_far in range(150):
        for last_ticket_type in range(3):
            if time_left <= minutes_left and cost_so_far >= cost_last_ticket:
                dp[last_ticket_type][time_left][cost_so_far - cost_last_ticket] = min(
                    dp[last_ticket_type][time_left][cost_so_far - cost_last_ticket],
                    dp[last_ticket_type][minutes_left][cost_so_far] + 20
                )
            minutes_left -= 1

print(min([dp[2][i][j] for i in range(max(10**9, n - 1) + 1) for j in range(max(150, 120))]))
