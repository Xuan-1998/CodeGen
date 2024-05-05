import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[float('inf')] * (2*s + 1) for _ in range(n)]
        for j in range(2*s+1):
            if j <= a[0]:
                dp[0][j] = min(dp[0][j], a[0] - j)
        
        for i in range(1, n):
            for j in range(2*s + 1):
                for k in range(max(0, j - (a[i-1] - s)), min(j, a[i])):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(a[i] - j, j - k))
        
        print(min(dp[-1]))

solve()
