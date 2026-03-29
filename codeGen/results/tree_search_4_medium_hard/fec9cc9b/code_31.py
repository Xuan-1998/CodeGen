import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i-1] = True
    for j in range(i+1, n+1):
        if arr[j-1] <= arr[j]:
            dp[i][j] = dp[i-1].index(True) < j - i
        else:
            for k in range(j-1, i-1, -1):
                if not dp[k][j-1]:
                    break
            else:
                dp[i][j] = True

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l][r] else "No")
