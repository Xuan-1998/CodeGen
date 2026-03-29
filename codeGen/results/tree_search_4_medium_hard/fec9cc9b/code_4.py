n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = True

for j in range(1, n):
    for i in range(j):
        if array[i] <= array[j]:
            dp[i][j] = max(dp[i][j], dp[i-1][i])

for _ in range(m):
    l, r = map(int, input().split())
    result = True
    for i in range(r, l - 1, -1):
        if not dp[i][i]:
            result = False
            break
    print("Yes" if result else "No")
