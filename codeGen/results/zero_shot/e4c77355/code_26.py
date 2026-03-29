n = int(input())
arr = list(map(int, input().split()))

dp = [[1 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n):
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            dp[i][j+1] = max(dp[i][j+1], dp[i-1][j]+1)

print(max(max(row) for row in dp))
