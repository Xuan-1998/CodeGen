import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] >= arr[j+1]:
            dp[i][j] = max(dp[i-1][k] for k in range(j) if dp[i-1][k] > 0 or (dp[i-1][k] == 0 and arr[k] >= arr[k+1])) + 1
        else:
            dp[i][j] = max(dp[i-1][k] for k in range(j, i) if dp[i-1][k] > 0 or (dp[i-1][k] == 0 and arr[k-1] >= arr[k]))

for _ in range(m):
    l, r = map(int, input().split())
    if all(arr[l:j+1] != sorted(arr[l:j+1]) for j in range(l, r+1)):
        print("Yes")
    else:
        print("No")
