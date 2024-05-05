n = int(input())
dp = [float('inf')] * (10**5 + 1)
dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[i], 20)
    for t in range(max(0, i - 14*60), i):
        remaining_time = i - t
        if remaining_time < 90:
            cost = dp[t] + 50
        else:
            cost = dp[t] + 120
        dp[i] = min(dp[i], cost)

print(*[dp[i] for i in range(n)], sep='\n')
