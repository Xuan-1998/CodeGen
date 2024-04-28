import sys

def recolor_lamps(n, s):
    dp = [[False] * 3 for _ in range(n + 1)]

    # Initialize base cases
    dp[0][s[0]] = True  # Single lamp always has same color
    dp[0][s[0]] = True

    for i in range(1, n + 1):
        for c in range(3):  # Colors: R, G, B
            if s[i - 1] == c:  # Same color as last lamp
                same_color = dp[i - 1][c]
            else:
                same_color = False

            # Explore possibilities: recolor all or leave some unchanged
            for j in range(3):
                if j != c and (not same_color or dp[i - 1][j]):
                    dp[i][j] = True
                    break

    r = sum([1 for row in dp[:n + 1] if not any(row)])
    t = ''
    for i, s in enumerate(s):
        if i < n and (not dp[i][0] or not dp[n - i - 1][2]):
            t += 'R' if s[0] == 'B' else 'G'
        else:
            t += s[0]

    print(r)
    print(t)

# Read input
n = int(input())
s = list(input())

recolor_lamps(n, s)
