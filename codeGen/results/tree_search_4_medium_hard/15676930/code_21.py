from collections import defaultdict

def hares(n, a, b, c):
    dp = defaultdict(int)
    dp[0][0] = 0
    for i in range(1, n+1):
        max_joy = 0
        for k in range(min(i, 2)+1):
            joy = (dp[i-1][k-1] if i>1 else 0) * b[i-1]
            if i > 1 and k < min(i-1, 2):
                joy += dp[i-2][k-1] * c[i-2]
            joy += (dp[i-1][k] if i>1 else 0) * a[i-1]
            max_joy = max(max_joy, joy)
        dp[i][0] = sum(a[:i])
        for j in range(1, min(i, 2)+1):
            dp[i][j] = max(dp[i][j], dp[i-1][k-1]*b[i-1]+dp[i-2][k-1]*c[i-2] if i>1 else 0)
    return dp[n][min(n, 2)]

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

print(hares(n, a, b, c))
