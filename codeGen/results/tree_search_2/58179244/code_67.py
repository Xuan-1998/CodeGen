def recolor(n, colors):
    dp = [[0] * 3 for _ in range(n)]
    prev_colors = [''] * (n + 1)

    for i in range(1, n + 1):
        for j in range(3):
            if i > 1:
                min_rec = float('inf')
                for k in range(3):
                    if k != int(colors[i - 2] == 'R' and colors[i - 2].upper() == 'G' or colors[i - 2].upper() == 'B'):
                        recolors, prev_colors[i] = recolor(i - 1, chr(ord('R') + k))
                        min_rec = min(min_rec, recolors)
                dp[i][j] = min_rec
            else:
                dp[i][0] = dp[i][1] = dp[i][2] = 0

    r = dp[n][0]
    t = ''
    for i in range(n):
        if i > 0 and dp[i][int(colors[i].upper() == 'R')] < r - dp[i - 1][int(colors[i - 1].upper() == 'R')]:
            t += chr(ord('R') + (colors[i].upper() == 'G' or colors[i].upper() == 'B'))
        else:
            t += colors[i]

    return str(r), t

n = int(input())
colors = input()
print(*recolor(n, colors))
