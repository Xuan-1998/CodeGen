import sys

def solve(n, s):
    dp = [[True] * (1 << n) for _ in range(n + 1)]
    win_team = [[False] * (1 << n) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1 << i, 1 << (i + 1)):
            if s[i - 1] == '1':
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = False

            win_team[i][j] = win_team[i - 1][j]
            for k in range(1 << i):
                if s[i - 1] == '0' and not win_team[i - 1][k]:
                    continue
                if s[i - 1] == '1':
                    j ^= (1 << i - 1)
                if dp[i][j] and not win_team[i - 1][k]:
                    win_team[i][j] = True

    print(*sorted([i for i in range(1 << n) if win_team[n][i]]), sep='\n')

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.read().strip()
    solve(n, s)
