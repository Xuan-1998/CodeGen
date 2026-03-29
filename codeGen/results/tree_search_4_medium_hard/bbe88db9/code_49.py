import sys

def solve():
    n = int(input())
    portals = list(map(int, input().split()))
    
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    dp[0][1] = 1
    
    for i in range(1, n+2):
        if i == 1:
            continue
        dp[i][1] = (dp[portals[i-2]][1] + dp[i-1][0]) % 1000000007
        for j in range(2, i+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000007
    
    print(dp[n+1][1])

if __name__ == "__main__":
    solve()
