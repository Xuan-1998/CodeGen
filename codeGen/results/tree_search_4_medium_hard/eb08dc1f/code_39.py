import sys

mod = 998244353

def last_digit(n):
    return int(str(n)[-1])

def prev_last_digit(x):
    if x == 0:
        return 9
    else:
        return 0

def extend(i, l):
    return (last_digit(i) == prev_last_digit(i - l)) + (extend(i - 1, l - 1) if i >= l and l > 1 else 0)

n = int(sys.stdin.readline())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(10):
    dp[0][1] = (dp[0][1] + 1) % mod

for i in range(1, n + 1):
    for l in range(2, min(i + 1, n + 1)):
        if l == 1:
            dp[i][l] = extend(i, l)
        else:
            dp[i][l] = (extend(i, l) - dp[i - l][l - 1] * 10 + int(dp[i - l][l - 1] != 0)) % mod

print(' '.join(map(str, [sum([dp[i][j] for j in range(1, i + 1)]) % mod for i in range(1, n + 1)])))
