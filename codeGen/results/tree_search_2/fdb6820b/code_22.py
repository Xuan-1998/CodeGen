from collections import defaultdict

dp = [[0]*(m+1) for _ in range(N+1)]
for i in range(m+1):
    dp[0][i] = 1

for num in array:
    for n in range(num, N+1):
        for k in range(1, m+1):
            if k >= len(array[:n]):
                dp[n][k] += dp[n-num][k-1]

print(sum(dp[N]))
