def garland_recoloring():
    n = int(input())
    s = input().strip()

    # Initialize dp table with infinite values
    dp = [[float('inf')] * 3 for _ in range(n + 1)]

    # Base case: only one lamp, so no recolors needed
    dp[1] = [0, 0, 0]

    for i in range(2, n + 1):
        for j in range(3):  # j is the color of the last lamp
            if s[i - 1] == 'R':
                c1, c2, c3 = dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]
            elif s[i - 1] == 'G':
                c1, c2, c3 = dp[i - 1][1], dp[i - 1][2], dp[i - 1][0]
            else:
                c1, c2, c3 = dp[i - 1][2], dp[i - 1][0], dp[i - 1][1]

            # If the current lamp is red and the last lamp was not red,
            # recoloring it to green or blue would make it diverse
            if j == 0:
                dp[i][j] = min(c1 + 1, c2)
            # If the current lamp is green and the last lamp was not green,
            # recoloring it to red or blue would make it diverse
            elif j == 1:
                dp[i][j] = min(c0 + 1, c2)
            # If the current lamp is blue and the last lamp was not blue,
            # recoloring it to red or green would make it diverse
            else:
                dp[i][j] = min(c0 + 1, c1)

    r = dp[n][0]
    t = s[:]

    for i in range(n - 1, 0, -1):
        if dp[i][s[i]] == r:
            t = 'R' if s[i] == 'G' else 'G' if s[i] == 'B' else 'B'
            r -= 1
        break

    print(r)
    print(t)

garland_recoloring()
