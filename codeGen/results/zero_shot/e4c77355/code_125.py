n = int(input())
arr = list(map(int, input().split()))
dp = [[1] * (max(arr) + 1) for _ in range(n)]

for i in range(n):
    for j in range(min(arr), max(arr) + 1):
        if arr[i] == j:
            dp[i][j] = 1
        elif i and dp[i-1][j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(max(max(row) for row in dp))
