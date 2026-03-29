import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(m-1, -1, -1):
            if 2*i <= n:
                dp[i][j] = sum(dp[k][max(0, j-k)] for k in range(i) if k >= i)
            else:
                dp[i][j] = math.pow(n, j-i+1, 10**9 + 7)
    ans = [0]
    for k in range(n):
        for l in range(m):
            ans.append((dp[k+1][l] - (0 if 2*(k+1) > n else sum(dp[max(0, i-1)][max(0, l-(i+1))] for i in range(k) if i >= k))) % (10**9 + 7))
    print(*ans, sep='\n')
