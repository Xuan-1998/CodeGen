import math

def num_squares(n):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for k in range(1, min(i, int(math.sqrt(i)) + 1)):
            if i == k ** 2:
                dp[i][k] = 1
            else:
                dp[i][k] = min(dp[i - j * j][j] + 1 for j in range(1, k + 1)) if i >= k ** 2 else dp[i - 1][k]
    
    return dp[n][-1]

n = int(input())
print(num_squares(n))
