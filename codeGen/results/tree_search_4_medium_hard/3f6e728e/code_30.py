import sys
from collections import defaultdict

input()
T = int(input())
mod = 10**9 + 7
dp = [[0] * (min(N, M) + 1) for _ in range(C + 1)]

for N, M, C in [list(map(int, input().split())) for _ in range(T)]:
    N, M, C = N - 1, M - 1, C
    upper_hemispheres = list(map(int, input().split()))
    lower_hemispheres = list(map(int, input().split()))

    for i in range(C + 1):
        dp[i][0] = 1

    for i in range(1, N + 1):
        for j in range(min(i, C), -1, -1):
            if j < upper_hemispheres[i - 1]:
                break
            dp[j][i] = (dp[j][i - 1] + dp[j][min(j - 1, M)]) % mod

    print(' '.join(map(str, [dp[i][N] for i in range(C + 1)])))
