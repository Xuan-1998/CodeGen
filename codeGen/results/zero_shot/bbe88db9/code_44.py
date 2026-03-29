import sys

def get_portal_moves():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().split()))
    
    dp = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if (dp[i-1] + 1) % 2 == 0:
            dp[i] = min(dp[i-1], dp[p[i-1]]) + 1
        else:
            dp[i] = min(dp[i-1], dp[i//2]+(i%2)) + 1
    
    print(dp[n])
