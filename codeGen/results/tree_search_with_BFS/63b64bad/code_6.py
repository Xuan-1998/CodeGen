python
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-1]*(n+1)
visited = [False]*(n+1)

for i in range(1, n+1):
    x = i
    y = 0
    path = []
    while 1 <= x <= n and dp[x] == -1:
        if visited[x]:
            dp[i] = -1
            break
        visited[x] = True
        path.append(x)
        y += a[x]
        x += a[x]
        if 1 <= x <= n and dp[x] == -1:
            y += a[x]
            x -= a[x]
    if dp[i] != -1:
        continue
    for j in range(len(path)-1, -1, -1):
        y += a[path[j]]
        if path[j] == x:
            break
    dp[i] = y

for i in range(1, n+1):
    print(dp[i])

