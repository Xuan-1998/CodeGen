def min_recolor_lamps():
    n = int(input())
    s = input()

    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        prev_color = (s[i - 1] == 'R') * 2 + ((s[i - 1] == 'G') * 1)
        same_color = (s[i - 1] == s[i - 2]) * 1
        for j in range(3):
            if j != prev_color:
                dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][prev_color]

    r = dp[n][0]
    t = [''] * n
    prev_color = (s[-1] == 'R') * 2 + ((s[-1] == 'G') * 1)
    for i in range(n - 1, -1, -1):
        if s[i] != t[i]:
            r -= 1
        t[i] = ['R', 'G', 'B'][dp[i][prev_color]]
        prev_color = (t[i] == 'R') * 2 + ((t[i] == 'G') * 1)

    print(r)
    print(''.join(t))

min_recolor_lamps()
