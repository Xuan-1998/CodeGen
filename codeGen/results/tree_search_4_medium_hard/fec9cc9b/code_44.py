import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i][0] = True
    for j in range(1, n - i + 2):
        if arr[j - 1] <= arr[j]:
            dp[i][j] = dp[i - 1][max(j - 1, 0)]
        else:
            dp[i][j] = not any(arr[k] > arr[j - 1] for k in range(j + 1, n))

for _ in range(m):
    l, r = map(int, input().split())
    if dp[r - l + 1][r]:
        print("Yes")
    else:
        print("No")
