import math

def solve():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 0
            else:
                min_squares = float('inf')
                for k in range(i - 1, -1, -1):
                    for side_length in range(math.ceil(math.sqrt((i-k) * (j-1))) + 1):
                        if (i-k) * (j-side_length) == side_length ** 2:
                            min_squares = min(min_squares, dp[k][j-side_length] + 1)
                dp[i][j] = min_squares

    print(dp[n][m])

if __name__ == "__main__":
    solve()
