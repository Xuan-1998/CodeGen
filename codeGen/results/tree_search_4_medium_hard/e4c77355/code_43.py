n = int(input())
arr = list(map(int, input().split()))

dp = [[1 for _ in range(10001)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 10001):
        if arr[i-1] > j:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

print(max([max(sub) for sub in dp[1]]))
