import sys

def solve(N, M, C):
    dp = [0] * (C + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(C, U_i - 1, -1):
            dp[j] += dp[j-1]
            if j < C:
                dp[j] %= (10**9 + 7)
    dp = [0] * (C + 1)
    dp[0] = 1
    for i in range(1, M + 1):
        for j in range(C, L_i - 1, -1):
            dp[j] += dp[j-1]
            if j < C:
                dp[j] %= (10**9 + 7)
    res = [0] * (C + 1)
    for i in range(1, N + 1):
        for j in range(C, U_i - 1, -1):
            res[j] += dp[j-1]
            if j < C:
                res[j] %= (10**9 + 7)
    return ' '.join(map(str, res))

T = int(sys.stdin.readline())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    U = list(map(int, sys.stdin.readline().split()))
    L = list(map(int, sys.stdin.readline().split()))
    print(solve(N, M, C))
