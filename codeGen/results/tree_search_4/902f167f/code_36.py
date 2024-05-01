===BEGIN CODE===
def min_squares(n, m):
    memo = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                memo[i][j] = 0
            elif i > 0 and j > 0:
                min_val = float('inf')
                for k in range(1, min(i, j) + 1):
                    if (i - k) ** 2 + (j - k) ** 2 <= (k + 1) ** 2:
                        min_val = min(min_val, memo[i - k][j - k] + 1)
                memo[i][j] = min_val
            else:
                memo[i][j] = float('inf')
    
    return memo[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
===END CODE===
