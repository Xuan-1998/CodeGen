import sys

def solve():
    n, m = map(int, input().split())
    c = int(input())

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        prev_char = None
        for j in range(1, m + 1):
            if i == 1:
                # First string
                dp[i][j] = (m - j) * c
            else:
                min_cost = sys.maxsize
                for k in range(j):
                    char_diff = ord(next_str[i-1][k]) - ord(prev_char)
                    if char_diff > 0:
                        cost = dp[i-1][k] + (j-k) * c
                        min_cost = min(min_cost, cost)
                    elif char_diff < 0:
                        cost = dp[i-1][k] + k * c
                        min_cost = min(min_cost, cost)
                dp[i][j] = min_cost
            prev_char = next_str[i-1][j-1]

    return dp[n][m]

next_str = [input() for _ in range(n)]
print(solve())
