===BEGIN CODE===
n = int(input())
dp = [[0]*n for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            min_val = float('inf')
            for k in range(j+1):
                min_val = min(min_val, dp[i-1][k])
            dp[i][j] += arr[i][j] + min_val

print(min(dp[-1]))
===END CODE===
