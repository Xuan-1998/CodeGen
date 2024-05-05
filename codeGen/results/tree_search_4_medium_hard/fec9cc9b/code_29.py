import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[False] * (n + 1) for _ in range(m)]

for i in range(n):
    dp[0][i] = True
for i in range(1, n):
    for j in range(i, n):
        if arr[i - 1] <= arr[j]:
            dp[0][j] = True

for l in range(1, m + 1):
    l, r = map(int, input().split())
    for i in range(l - 1, r):
        if not dp[l - 1][i]:
            break
    else:
        print("Yes")
    for j in range(r - 1, l - 1, -1):
        if arr[j] < arr[j - 1]:
            break
    else:
        print("No")
