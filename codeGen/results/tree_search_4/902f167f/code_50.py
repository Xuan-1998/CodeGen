from sys import stdin

def min_squares(n, m):
    max_size = int((n // 2) + (m // 2))  # Maximum possible side length of squares
    dp = [[[float('inf')] for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = [0]
            else:
                for k in range(1, min(i, j) + 1):
                    # Calculate the minimum number of squares needed
                    if i >= k and j >= k:
                        place_at_corner = dp[k-1][k-1][max_size - k]
                        place_elsewhere = dp[i-k][j-k][max_size - k]
                        dp[i][j].append(min(place_at_corner, place_elsewhere) + 1)
                    else:
                        dp[i][j].append(dp[i-k][j-k][max_size - k])

    return min(dp[n][m])

n, m = map(int, stdin.readline().split())
print(min_squares(n, m))
