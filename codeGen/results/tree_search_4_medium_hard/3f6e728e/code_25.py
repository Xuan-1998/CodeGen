import sys

MOD = 10**9 + 7
T = int(input())

for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    dp = [0] * (C + 1)
    dp[0] = 1

    for i in range(1, C + 1):
        if i <= U[0]:
            dp[i] = (dp[i-1] + len([x for x in L if x <= i])) % MOD
        else:
            dp[i] = dp[i-1]

    print(*dp, sep=' ')
