import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if arr[j - 1] > arr[j]:
            dp[i][j] = 1
        else:
            k = max(k for k in range(j) if arr[k] <= arr[j])
            dp[i][j] = dp[i][k] + (arr[k - 1] != arr[j])

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l][r] > 0 else "No")
