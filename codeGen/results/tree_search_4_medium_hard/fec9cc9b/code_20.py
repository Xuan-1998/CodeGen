import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[False] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = True
    if i > 0 and arr[i] >= arr[i-1]:
        dp[i-1][i] = True

for length in range(3, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        if arr[j] >= arr[j-1] and all(arr[k] < arr[k+1] or arr[k] == arr[k+1] for k in range(i, j)):
            dp[i][j] = True

for _ in range(m):
    l, r = map(int, input().split())
    if any(dp[l-1][k-1] and all(arr[k] < arr[k+1] or arr[k] == arr[k+1] for k in range(k, r)) for k in range(l-1)):
        print("Yes")
    else:
        print("No")
