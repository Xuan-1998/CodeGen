n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i + 1):
        if a[j] <= a[j + 1]:
            dp[i][j] = max(dp[i - 1][k - 1] for k in range(j + 1, i + 1) if a[k - 1] <= a[k]) + 1
        else:
            dp[i][j] = dp[i - 1][j]

for q in range(m):
    l, r = map(int, input().split())
    if dp[r][l - 1] == r - l + 1:
        print("Yes")
    else:
        print("No")
