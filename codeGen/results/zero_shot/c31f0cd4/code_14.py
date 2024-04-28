n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)
dp = [[0] * (total_sum + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(total_sum + 1):
        if arr[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1]] + arr[i - 1])
ans = set()
for i in range(total_sum // 2, -1, -1):
    if dp[n][i] == i:
        ans.add(i)
print(*sorted(ans), sep=' ')
