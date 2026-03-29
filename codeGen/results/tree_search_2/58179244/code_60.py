def solve():
    n = int(input())
    colors = list(input())

    # Initialize 2D array dp
    dp = [[float('inf')] * 3 for _ in range(n+1)]

    # Base case: No recoloring needed initially
    dp[0][0] = dp[0][1] = dp[0][2] = 0

    for i in range(1, n+1):
        for prev_color in range(3):
            if colors[i-1] == chr(ord('R') + prev_color):
                # If the current lamp has the same color as the previous one
                for new_color in set(colors):
                    if new_color != chr(ord('R') + prev_color):
                        dp[i][prev_color] = min(dp[i][prev_color], 1 + dp[i-1][ord(new_color) - ord('R')])
            else:
                # If the current lamp has a different color than the previous one
                dp[i][prev_color] = dp[i-1][prev_color]

    # Find the minimum number of recolors needed
    min_rec_colors = float('inf')
    for prev_color in range(3):
        min_rec_colors = min(min_rec_colors, dp[n][prev_color])

    # Construct a diverse garland with the minimum number of recolors
    t = []
    i = n - 1
    while i > 0:
        prev_color = (dp[i][0] + dp[i][1] + dp[i][2]) % 3
        t.append(chr(ord('R') + prev_color))
        i -= 1

    # Print the result
    print(min_rec_colors)
    print(''.join(reversed(t)))

solve()
