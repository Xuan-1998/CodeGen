code block:
def solve(n):
    dp = [[0.0 for _ in range(2)] for _ in range(n+1)]
    
    def f(i, j):
        if i == 0:
            return p[i][j]
        else:
            return (p[i][0] * dp[i-1][0] + p[i][1] * dp[i-1][1]) / (p[i][0] + p[i][1])
    
    for i in range(n+1):
        if i == 0:
            dp[i][0] = p[i][0]
            dp[i][1] = p[i][1]
        else:
            dp[i][0] = f(i, 0)
            dp[i][1] = f(i, 1)
    
    return (dp[n][0] + dp[n][1]) / 2.0

T = int(input())
for _ in range(T):
    n = int(input())
    p = [[0 for _ in range(2)] for _ in range(n)]
    for i in range(n):
        p[i] = [float(x) for x in input().split()]
    
    print(solve(n))
