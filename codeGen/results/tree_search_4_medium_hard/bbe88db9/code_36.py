import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize base case: dp[0][0] = 1
    dp[0][0] = 1
    
    # Fill up the DP table
    for i in range(1, n + 1):
        if p[i - 1] > 0:
            dp[i][0] = dp[i - 1][1]
        else:
            dp[i][0] = dp[i - 1][0]
        
        for j in range(1, i + 1):
            # Use second portal if ceiling has odd number of crosses
            if (dp[i - 1][j - 1] % 2 != 0) or (i == n):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + 1
            # Use first portal otherwise
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Print the minimum number of moves needed to reach room n+1 with ceiling having no crosses
    print(dp[n][0])

if __name__ == "__main__":
    solve()
