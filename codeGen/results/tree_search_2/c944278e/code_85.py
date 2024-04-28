import sys

def solve():
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().strip()))

    dp = [[0] * (1 << n) for _ in range(n + 1)]
    win_teams = []

    for i in range(1, n + 1):
        for j in range((1 << i) - 1, -1, -1):
            if s[i - 1]:
                # If the current team wins, add its skill level to dp
                dp[i][j] = dp[i - 1][j | (1 << (i - 1))] + 2**(n - i)
            else:
                # If the current team loses, consider all possible outcomes
                for k in range((1 << i) - 1):
                    if j & (1 << k):
                        dp[i][j] = max(dp[i][j], dp[i - 1][k])
                    else:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k | (1 << (i - 1))])

    for i in range((1 << n) - 1, -1, -1):
        if dp[n][i]:
            win_teams.append(i)

    print(' '.join(map(str, win_teams)))

if __name__ == '__main__':
    solve()
