max_val = int(input())
n = len([int(x) for x in input().split()])
dp = [[0] * (max_val + 1) for _ in range(n + 1)]

for k in range(1, n + 1):
    for j in range(max_val + 1):
        if dp[k-1][j]:
            if j < arr[k-1]:  # arr[k] is an increase from arr[k-1]
                dp[k][j] = max(dp[k-1][j], dp[k-1][arr[k-1]] + 1)
            else:
                dp[k][j] = dp[k-1][j]

print(max(map(max, dp)))
