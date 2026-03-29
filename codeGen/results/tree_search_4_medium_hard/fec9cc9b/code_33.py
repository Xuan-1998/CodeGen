n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]

for i in range(1, n):
    if array[i-1] <= array[i]:
        dp[i][i-1] = [True, True]
    else:
        dp[i][i-1] = [False, False]

for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if not dp[j][j-1][0]:
            dp[i][j] = [False, True]
        elif not dp[i][j-1][1]:
            dp[i][j] = [True, False]

for _ in range(m):
    l, r = map(int, input().split())
    if not (dp[l-1][r-1][0] and not dp[l-1][r-1][1]):
        print("No")
    else:
        print("Yes")
