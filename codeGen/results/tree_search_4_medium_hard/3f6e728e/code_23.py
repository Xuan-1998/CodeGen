import math

mod = 10**9 + 7

def solve():
    C = int(input())
    dp = [0] * (C + 1)
    dp[0] = 1
    for i in range(2, C + 1):
        dp[i] = sum(dp[j] * math.comb(C_index.index(j), j) for j in range(i)) % mod
        if i in U_count:
            dp[i] += sum(dp[j] * U_count.get(j, 0) for j in range(i)) % mod
    print(*dp[1:], sep=' ')

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U_count = {}
    for _ in range(N):
        u = int(input())
        if u not in U_count:
            U_count[u] = 0
        U_count[u] +=1
    L_count = {}
    for _ in range(M):
        l = int(input())
        if l not in L_count:
            L_count[l] = 0
        L_count[l] +=1
    C_index = sorted(U_count.keys() + L_count.keys())
    solve()
