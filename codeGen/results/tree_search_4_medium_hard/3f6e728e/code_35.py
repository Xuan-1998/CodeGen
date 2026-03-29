import sys

def find_lower_hemisphere(r):
    return sum(1 for _ in range(min(M, N)) if L_[:] <= r)

def solve(N, M, C, U_, L_):
    memo = {}
    dp = [[0] * (min(N, M) + 1) for _ in range(C + 1)]

    for i in range(C, -1, -1):
        for j in range(min(N, M) + 1):
            if i == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = sum(dp[k][max(0, j-m)] for k in range(C, 0, -1) if k <= i and find_lower_hemisphere(k) >= m)
                memo[(i, j)] = dp[i][j]
    return [str((dp[C][j]) % (10**9 + 7)) for j in range(min(N, M))]

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U_ = list(map(int, input().split()))
    L_ = list(map(int, input().split()))
    print(*solve(N, M, C, U_, L_), sep=' ')
