n = int(input())
arr = list(map(int, input().split()))
dp = [[1] * (n+1) for _ in range(n+1)]
ans = [0] * n
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[j-1] > arr[i-1]:
            dp[i][j] = max(dp[i-1][k] + 1 for k in range(j) if arr[k] < arr[j-1]) + 1
        else:
            dp[i][j] = dp[i-1][j]
max_len = max(max(row) for row in dp)
ans = [row.count(max_len) for row in dp].count(max(ans))
print(ans)
