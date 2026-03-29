import sys

def solution():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        dp = [[0, 0] for _ in range(n+1)]
        
        # Compute dp values
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) - a[i-1]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + x - a[i-1]
        
        # Print the maximum sum
        print(max(dp[-1]))

solution()
