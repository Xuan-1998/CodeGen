===BEGIN CODE===
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(min(i, n), -1, -1):
    if a[j-1] >= a[i-1]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)
    else:
      dp[i][j] = 0

for _ in range(m):
  l, r = map(int, input().split())
  if dp[r][r-l+1] > 0:
    print("Yes")
  else:
    print("No")
===END CODE===
