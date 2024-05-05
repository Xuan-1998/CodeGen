import sys
input = lambda: [int(x) for x in input().split()]

n, m = input()
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1
for l in range(1, n + 1):
    for r in range(l, n + 1):
        if arr[r - 1] <= arr[r]:
            dp[l][r] = max(dp[k][r - 1] for k in range(l, r)) + 1
        else:
            dp[l][r] = 0

for _ in range(m):
    l, r = input()
    print("Yes" if dp[l][r] > 0 else "No")
