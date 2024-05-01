import math

def min_squares(n, m):
    # Pre-compute all square numbers up to sqrt(max(n*m))
    max_val = int(math.sqrt(n * m))
    squares = [i ** 2 for i in range(1, max_val + 1)]

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            min_count = float('inf')
            for k in range(i):
                for square_size in range(j):
                    if (i - k) * (j - square_size) in squares:
                        min_count = min(min_count, dp[k][square_size] + 1)
            dp[i][j] = min_count

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
