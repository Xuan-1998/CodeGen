import sys

def solve(n, c):
    dp = [[0] * (c + 1) for _ in range(n)]

    # Initialize base cases
    for j in range(c + 1):
        dp[0][j] = 0

    for i in range(1, n):
        s_i = int(input())
        for j in range(c + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= s_i:
                dp[i][j] += min(s_i, j)

    # Read queries
    q = int(input())
    for _ in range(q):
        t, x1i, y1i, x2i, y2i = [int(x) for x in input().split()]
        total_brightness = 0

        # Calculate the total brightness within the current view
        for i in range(min(n - 1, x2i), max(0, x1i)):
            for j in range(min(c, y2i), max(0, y1i) + 1):
                if dp[i][j] > total_brightness:
                    total_brightness = dp[i][j]

        print(total_brightness)

if __name__ == "__main__":
    n, c, q = map(int, input().split())
    solve(n, c)
