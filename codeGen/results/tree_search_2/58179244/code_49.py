import sys
from collections import defaultdict

def solve():
    n = int(input())
    prev_colors = list(input())

    dp = [[0] * 3 for _ in range(n+1)]
    next_prev_colors = defaultdict(int)

    for i in range(1, n+1):
        for j in range(3):
            dp[i][j] = min([dp[i-1][k] + (1 if k != j else 0) for k in range(3)])
            next_prev_colors[prev_colors[i-1]] += 1

    print(dp[n][0]) # minimum number of recolors
    print(''.join(['R' if c == 0 else 'G' if c == 1 else 'B' for c in dp[n]])) # diverse garland

if __name__ == "__main__":
    solve()
