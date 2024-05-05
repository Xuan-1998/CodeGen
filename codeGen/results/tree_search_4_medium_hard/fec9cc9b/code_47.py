n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = 1
    for j in range(i-1, -1, -1):
        if a[j] <= a[j+1]:
            dp[j][i] = max(dp[j][i], dp[j+1][i]+1)
ladder = [[False]*n for _ in range(n)]
for i in range(2, n+1):
    for j in range(i-1, -1, -1):
        if a[j] <= a[j+1]:
            ladder[j][i] = (dp[j][i]%2==1)
queries = [list(map(int, input().split())) for _ in range(m)]
for l, r in queries:
    print("Yes" if ladder[l-1][r] else "No")
