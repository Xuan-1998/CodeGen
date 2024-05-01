import math

def min_squares(n, m):
    dp = [[math.inf] * (m + 1) for _ in range(n + 1)]
    
    # Base case: no squares needed to tile the first row
    for j in range(m + 1):
        dp[0][j] = 0
    
    # Fill in the dp array using a bottom-up approach
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i):
                for m in range(j):
                    if (i - k) * (j - m) == int(math.sqrt((i - k) * (j - m))) ** 2:
                        dp[i][j] = min(dp[i][j], dp[k-1][m-1] + 1)
    
    return dp[n][m]

# Example usage
n, m = map(int, input().split())
print(min_squares(n, m))
