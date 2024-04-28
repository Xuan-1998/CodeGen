import sys

def solve():
    n = int(input())
    s = input()

    dp = [[0] * 3 for _ in range(n)]
    prev_colors = [0] * (n + 1)
    prev_colors[0] = -1  # sentinel value

    for i in range(1, n + 1):
        if s[i-1] == 'R':
            curr_color = 0
        elif s[i-1] == 'G':
            curr_color = 1
        else:
            curr_color = 2

        prev_color = prev_colors[i-1]
        next_color = (curr_color + 1) % 3 if prev_color != curr_color else (curr_color + 2) % 3

        dp[i][curr_color] = min(dp[i-1][prev_color] + 1, dp[i-1][next_color])

    r = dp[-1][0]
    t = ''
    curr_color = 0
    for i in range(n):
        prev_color = curr_color
        if s[i] == 'R':
            curr_color = 0
        elif s[i] == 'G':
            curr_color = 1
        else:
            curr_color = 2

        t += ['RGB'[curr_color]] * (dp[i+1][curr_color] - dp[i][prev_color])
    print(r)
    print(t)

if __name__ == "__main__":
    solve()
