import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0, 0] for _ in range(n + 2)]
    dp[1][0] = 1
    
    for i in range(2, n + 2):
        if not dp[i - 1][1]:
            dp[i][0] = min(dp[p[i - 1]][0], dp[p[i - 1]][1]) + 1
            dp[i][1] = dp[i - 1][0] + 1
        else:
            dp[i][0] = dp[p[i - 1]][1]
            dp[i][1] = dp[i - 1][0] + 1
    
    print(dp[n + 1][1])

solve()
