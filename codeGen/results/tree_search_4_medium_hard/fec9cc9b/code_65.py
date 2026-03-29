n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if all(a[k-1] <= a[k] for k in range(j)):
            dp[i][j] = True

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l-1][r] else "No")
