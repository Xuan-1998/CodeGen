n = int(input())
a = list(map(int, input().split()))
dp = [[-1]*n for _ in range(n)]

def transition(x):
    x = (x+a[x-2]) % n
    return x, a[x-2]

for i in range(2, n+1):
    for j in range(i):
        if dp[i][j] == -1:
            dp[i][j], _ = transition(j)
            dp[i][j] = max(dp[i][j], dp[j][j-1]+a[j])
        else:
            dp[i][j] = max(dp[i][j], a[j])

for i in range(2, n+1):
    print(dp[n][i-1])
