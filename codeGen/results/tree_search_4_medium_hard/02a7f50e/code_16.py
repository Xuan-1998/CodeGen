from collections import defaultdict

dp = defaultdict(dict)
n, = map(int, input().split())
for i in range(1, n+1):
    b_i, = map(int, input().split())
    for j in range(max(b_i) + 1):
        if dp[i-1][j] is None:
            dp[i-1][j] = float('inf')
        for k in range(i):
            if b_k <= j:
                dp[i][j] = min(dp[k][min(b_k, j)] + (i-k) for k in range(k+1))
                break
        else:
            dp[i][j] = min(dp[k][min(b_k, j)] + (i-k) for k in range(i))

print(min(dp[n].values()))
