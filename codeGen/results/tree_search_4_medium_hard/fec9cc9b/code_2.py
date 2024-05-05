import sys

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]

# Initialize base case
dp[0][n-1] = True

for i in range(1, n):
    dp[i][i] = True

for r in range(n):
    j = r
    while j >= 0 and array[j] <= array[j-1]:
        j -= 1
    if j >= 0:
        for l in range(j+1):
            if not dp[l][j]: break
        dp[l][r] = True

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l][r] else "No")
