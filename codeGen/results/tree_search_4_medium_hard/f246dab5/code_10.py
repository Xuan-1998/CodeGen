n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 20

for i in range(1, n + 1):
    t = min((max(dp[i - 1], (i - 1) // 60 * (50 if (i - 1) % 60 < 90 else 120)) + 20,
             dp[max(0, i - 91)] or t +
             (min(i, 1440) - max(0, i - 90)) // 60 * (50 if min(i, 1440) % 60 < 90 else 120))
    print(int(t))
