def diverse_lamp_garland():
    n = int(input())
    colors = list(input())

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        same_color = colors[i] == colors[(i - 1) % n]
        diff_color = 'RGB'.index(colors[i]) != 'RGB'.index(colors[(i - 1) % n])

        if same_color:
            dp[i + 1] = min(dp[i + 1], dp[i] + (1 if i == 0 else 2))
        elif diff_color:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    print(min(dp[-1:]))

    # Generate a diverse garland with the minimum number of recolors
    result_colors = list(colors)
    for i in range(1, n):
        if (dp[i - 1] < dp[i]):
            if colors[i-1] == 'R':
                result_colors[i-1], result_colors[i] = 'G', 'B'
            elif colors[i-1] == 'G':
                result_colors[i-1], result_colors[i] = 'B', 'R'
            else:
                result_colors[i-1], result_colors[i] = 'R', 'G'

    print(''.join(result_colors))

diverse_lamp_garland()
