python
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-1]*(n+1)
dp[1] = 0
vis = [0]*(n+1)

for i in range(2, n+1):
    path = []
    while i > 0 and i <= n and dp[i] == -1:
        if vis[i]:
            for j in path:
                dp[j] = -1
            break
        vis[i] = 1
        path.append(i)
        i += a[i]
    else:
        val = dp[i]
        for j in reversed(path):
            val += a[j]
            dp[j] = val

for i in dp[2:]:
    print(i)

