import sys
from collections import defaultdict

def min_replant(n, m):
    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    species_count = defaultdict(int)
    
    # Count the number of plants for each species
    for i in range(n):
        species_count[int(input())] += 1
    
    # Fill up the dynamic programming table
    for i in range(1, m + 1):
        for j in range(i, n + 1):
            for k in range(1, m + 1):
                if species_count[k] > 0:
                    dp[i][j][k] = min(dp[i-1][j-k][k] + k - 1 if k > 0 else k, 
                                       dp[i-1][j][k] + j - i if k == 0 else k)
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    
    return dp[m][n][m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_replant(n, m))
