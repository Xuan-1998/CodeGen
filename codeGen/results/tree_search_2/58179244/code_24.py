import sys

def min_recolors(s):
    n = len(s)
    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        c = s[i - 1]
        if i == 1:
            dp[i][c] = (c != 'R') + (c != 'G')
        else:
            dp[i][c] = min(dp[i-1][c] + (c != s[i-2]), 1 + dp[i-1][s[i-2]])

    r = dp[-1].index(min(dp[-1]))
    t = ''.join(['R', 'G', 'B'][c] for c in dp[-1])

    return str(r) + '\n' + t

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(min_recolors(s))
