import sys

def make_zeros():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = [[False] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for k in range(1, n+1):
        for i in range(k, -1, -1):
            dp[i][k] = min(dp[i-1][k-1], dp[i][0]) or dp[i-k][k]
    
    print("YES" if dp[n][0] else "NO")

make_zeros()
