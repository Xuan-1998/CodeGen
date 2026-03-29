from sys import stdin

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for x in range(2, n + 1):
        for y in range(n + 1):
            if a[x - 1] > y:
                continue
            if x <= 0 or x > n:
                return y
            dp[x][y] = min(dp[max(x - a[x - 1], 1)][y + a[x - 1]], dp[x - a[x - 1]][y]) + a[x - 1]
    
    return dp[n][n - 1]

print(solve())
