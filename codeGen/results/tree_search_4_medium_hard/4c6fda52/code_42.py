def solve():
    n, k = map(int, input().split())
    s = input()
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(k):
        if i == 0:
            dp[0][i] = i
        else:
            dp[0][i] = k-1
    for i in range(1, n+1):
        for j in range(min(i, k)):
            if s[i-j-1:i+1].count('R') + s[i-j-1:i+1].count('G') + s[i-j-1:i+1].count('B') <= 2:
                dp[i][j] = min(dp[i-1][j], dp[i-1][k-j-1]+(s[i-k:i].count('R') + s[i-k:i].count('G') + s[i-k:i].count('B')))
    return sum(dp[n-1][0] for _ in range(q))

q = int(input())
for _ in range(q):
    print(solve())
