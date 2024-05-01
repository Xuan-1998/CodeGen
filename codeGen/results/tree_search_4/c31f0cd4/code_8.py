from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
max_sum = sum(arr)

dp = [[False for _ in range(max_sum + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True
for i in range(1, n + 1):
    for j in range(1, max_sum + 1):
        if arr[i - 1] <= j:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        else:
            dp[i][j] = dp[i - 1][j]

ans = set()
for i in range(1, max_sum + 1):
    if dp[n][i]:
        ans.add(i)
print(*sorted(list(ans)), sep=' ')
