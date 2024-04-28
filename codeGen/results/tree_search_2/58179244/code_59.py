def min_recolor_lamps():
    n = int(input())
    s = input().strip()

    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][set()] = 0

    c = set()
    for i, color in enumerate(s):
        if color not in c:
            c.add(color)
            dp[i+1][c] = min(dp[i][c], dp[i][c].copy() + (3 - list(c).count(color),))
        else:
            dp[i+1][c] = dp[i][c]

    r = dp[-1][set()]
    t = ''
    c = set()
    for i in range(n-1, -1, -1):
        if dp[i][c] == r:
            break
        color = 'R' if 0 in c else 'G' if 1 in c else 'B'
        t += color
        c.add(color)
        r -= 1

    print(r)
    print(t[::-1])
