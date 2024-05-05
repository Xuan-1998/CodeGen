import sys
from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        # Initialize base case
        prefix_sum = 0
        for i in range(n):
            prefix_sum += a[i]
            dp[i][0] = prefix_sum
        
        for j in range(1, k + 1):
            for i in range(z, n):
                if j - 1 < z:
                    # Consider moving left or right
                    dp[i][j] = max(dp[i-1][min(j-1, z)] + a[i], 
                                   dp[i-1][j-1] + a[i])
                else:
                    # Only consider moving right
                    dp[i][j] = dp[i-1][j-1] + a[i]
        
        print(max(dp[-1]))


if __name__ == "__main__":
    solve()
