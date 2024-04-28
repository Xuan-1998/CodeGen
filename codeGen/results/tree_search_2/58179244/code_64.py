from collections import defaultdict

def min_recoloring():
    n = int(input())
    colors = list(input())

    dp = [defaultdict(int) for _ in range(n + 1)]

    for i in range(2, n):
        prev_color = colors[i - 1]
        curr_color = colors[i]

        if prev_color == curr_color:
            recolors = min(dp[i - 1][prev_color] + 1, dp[i - 1].get('R') or dp[i - 1].get('G') or dp[i - 1].get('B'))
        else:
            recolors = 0

        dp[i][curr_color] = min(dp[i-1][prev_color] + (1 if prev_color != curr_color else 2), dp[i-1].get('R') or dp[i-1].get('G') or dp[i-1].get('B'))

    recolors = dp[-1]['R'] if colors[0] == 'R' else min(dp[-1].values())

    diverse_colors = ['R', 'G', 'B'][list(dp[-1].values()).index(recolors)]

    print(recolor, end='\n')
    for i in range(n):
        if dp[i][colors[i]] != recolors:
            colors[i] = diverse_colors
    print(''.join(colors), end='\n')

if __name__ == "__main__":
    min_recoloring()
