python
n = int(input().strip())
a = [0] + list(map(int, input().strip().split()))
dp = [-2]*(n+1)
dp[1] = 0
visited = [False]*(n+1)

for i in range(1, n+1):
    if dp[i] == -2:
        x, y = i, 0
        path = []
        while 1 <= x <= n and dp[x] == -2:
            if visited[x]:
                for j in path:
                    dp[j] = -1
                break
            visited[x] = True
            path.append(x)
            y += a[x]
            x += a[x]
        else:
            if dp[x] == -2:
                dp[x] = y
            for j in path:
                dp[j] = dp[x] if dp[j] == -1 else y + dp[x]

for i in range(2, n+1):
    print(dp[i])

