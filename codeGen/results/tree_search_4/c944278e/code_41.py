import sys

def solve(n, s):
    dp = [[False] * (1 << n) for _ in range(n)]
    res = [[] for _ in range(n)]

    for i in range(n):
        for j in range(1 << n):
            if (s[i] & (1 << (j % 2))) == 0:
                dp[i][j] = False
            else:
                dp[i][j] = True
            if j > 0 and dp[i][j - 1]:
                dp[i][j] = True

        for j in range(1 << n):
            res[i].append(j) if dp[i][j] else None

    return [team for phase in res for team in (phase,)]

n = int(sys.stdin.readline())
s = ''.join([c for c in sys.stdin.readline().strip()])

print('\n'.join(map(str, solve(n, s))))
