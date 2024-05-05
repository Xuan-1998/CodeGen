import math

def comb(n, k):
    return math.comb(n, k) % (10**9 + 7)

def memoize(dp, i):
    if dp[i] is not None:
        return dp[i]
    result = 0
    for j in range(1, min(i+1, len(U_count))): 
        count = U_count[j]
        binom_coeff = comb(count, U_count.count(j))
        result += dp[j-1]*binom_coeff
    dp[i] = result % (10**9 + 7)
    return dp[i]

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U_count = {}
    for _ in range(N):
        u = int(input())
        if u not in U_count: 
            U_count[u] = 1
        else:
            U_count[u] += 1
    L_count = {}
    for _ in range(M):
        l = int(input())
        if l not in L_count: 
            L_count[l] = 1
        else:
            L_count[l] += 1

    dp = [0] * (C+1)
    dp[0] = 1

    for i in range(1, C+1):
        memoize(dp, i)

    print(*dp, sep=' ')
