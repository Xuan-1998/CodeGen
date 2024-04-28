n = int(input())
arr = list(map(int, input().split()))
dp = [[[] for _ in range(sum(arr) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, sum(arr) + 1):
        if arr[i - 1] <= j:
            dp[i][j] = (dp[i - 1][j - arr[i - 1]] or [arr[i - 1]]) + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]
print(*set(sum(subset) for subset in dp[-1]))
