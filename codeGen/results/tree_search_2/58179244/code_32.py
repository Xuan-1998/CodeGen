import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    dp = [[False] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        same_color = (s[i - 1] == s[0])
        if i < 2:
            dp[i][0] = not same_color
            dp[i][1] = not same_color
            dp[i][2] = not same_color
        else:
            for j in range(3):
                dp[i][j] = (dp[i - 1][0] and s[0] != chr(ord('R') + j)) or \
                           (dp[i - 1][1] and s[0] != chr(ord('G') + j)) or \
                           (dp[i - 1][2] and s[0] != chr(ord('B') + j))

    min_recolors = n
    for i in range(1, n + 1):
        if dp[i][0]:
            min_recolors = i
            break

    sys.stdout.write(str(min_recolors) + '\n')
    sys.stdout.write(s[:min_recolors] + 'R' * (n - min_recolors) + '\n')

solve()
