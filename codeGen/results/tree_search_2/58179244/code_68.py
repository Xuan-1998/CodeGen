import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    # Initialize the table with base cases
    dp = [[0] * 3 for _ in range(n + 1)]
    prev_colors = [''] * (n + 1)

    # Fill in the rest of the table
    for i in range(1, n + 1):
        if s[i - 1] == 'R':
            curr_color = 0
        elif s[i - 1] == 'G':
            curr_color = 1
        else:
            curr_color = 2

        if prev_colors[i - 1] != '':
            prev_color = {'R': 1, 'G': 0, 'B': 2}[prev_colors[i - 1]]
        else:
            prev_color = curr_color

        dp[i][curr_color] = min(dp[i-1][prev_color], 1) if s[i - 1] != s[i - 2] else dp[i-1][prev_color]
        prev_colors[i] = 'RGB'[curr_color]

    # Output the minimum number of recolors and a diverse garland
    r = dp[n][0]
    t = ['R' if c == 0 else 'G' if c == 1 else 'B' for c in s]
    sys.stdout.write(str(r) + '\n')
    sys.stdout.write(''.join(t) + '\n')

if __name__ == '__main__':
    solve()
