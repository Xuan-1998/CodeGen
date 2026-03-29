from collections import defaultdict

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = defaultdict(lambda: defaultdict(int))
    dp[1][0] = 1
    
    for i in range(2, n+2):
        if (dp[i-1][p[i-1]%i].count(1) % 2 == 0):
            dp[i][0] = dp[i-1][p[i-1]%i]
        else:
            dp[i][0] = min(dp[i-1][k] for k in range(i)) + 1
        dp[i][1] = min(dp[i-1][k] for k in range(i))
    
    print((dp[n+1][p[n]%n].count(1) % 2 == 0) * (min(dp[n+1][k] for k in range(n+1)) + 1))
