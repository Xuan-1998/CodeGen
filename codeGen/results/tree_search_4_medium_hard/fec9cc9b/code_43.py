n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0]*m for _ in range(n)]

for i in range(1, n):
    if arr[i] <= arr[i-1]:
        dp[i][i] = 1
    else:
        dp[i][i] = 0

for r in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[r-l+1][r-1] == 1 else "No")
