import sys

def diverse_garland():
    n = int(input())
    s = input()

    # Initialize 2D array DP_state[][] with zeros
    dp = [[0] * 3 for _ in range(n + 1)]

    # Fill the base case (first lamp)
    for i in range(3):
        if s[0] == 'R' and i == 0:
            dp[1][i] = 2
        elif s[0] == 'G' and i == 1:
            dp[1][i] = 2
        else:
            dp[1][i] = 1

    # Fill the rest of the DP table using bottom-up dynamic programming
    for i in range(2, n + 1):
        for j in range(3):
            if s[i - 1] == 'R' and j == 0:
                dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + 1
            elif s[i - 1] == 'G' and j == 1:
                dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + 1
            else:
                dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + 1

    # Find the minimum number of recolors needed to make the garland diverse
    r = sys.maxsize
    t = ''
    for i in range(3):
        if dp[n][i] < r:
            r = dp[n][i]
            t = 'R' if i == 0 else 'G' if i == 1 else 'B'

    print(r)
    print(t * n)

diverse_garland()
