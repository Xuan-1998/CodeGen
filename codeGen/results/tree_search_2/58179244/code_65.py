def min_recolor(n, s):
    dp = [[0 if i == 0 else float('inf') for _ in range(3)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 0
        dp[i][2] = 0

    for i in range(1, n + 1):
        if s[i - 1] == 'R':
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + (1 if i > 1 else 0)
        elif s[i - 1] == 'G':
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + (1 if i > 1 else 0)
        elif s[i - 1] == 'B':
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + (1 if i > 1 else 0)

    r = min(dp[n])
    
    t = ''
    prev_color = s[0]
    for i in range(n):
        if dp[n][0] == dp[i][prev_color]:
            t += s[i] + 'R' if prev_color == 'G' or prev_color == 'B' else s[i]
            prev_color = (1 if prev_color == 'R' else 2) % 3
        elif dp[n][2] == dp[i][prev_color]:
            t += s[i] + 'B' if prev_color == 'G' else s[i] + 'G'
            prev_color = (2 if prev_color == 'R' else 1) % 3
        else:
            t += s[i]
    return str(r) + '\n' + t

# Read input from standard input
n = int(input())
s = input()

print(min_recolor(n, s))
