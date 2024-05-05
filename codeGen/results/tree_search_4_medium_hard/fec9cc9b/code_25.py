n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = True
    if array[i-1] <= array[i]:
        dp[i][i] = True

for l in range(1, n+1):
    for r in range(l, n+1):
        if not dp[l][r]: continue
        for i in range(l, r):
            if array[i-1] > array[i] or array[r-1] < array[i]:
                dp[l][r] = False; break

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[l][r] else "No")
