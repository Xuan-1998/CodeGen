import sys

mod = 10**9 + 7

def solve(N, M, C, U, L):
    dp = [[0] * (C + 1) for _ in range(C + 1)]

    dp[0][j] = 1 if j == 0 else 0
    for i in range(1, C + 1):
        dp[i][0] = 1
        for j in range(1, min(i, C)):
            if any(U_k <= j for U_k in U) and any(L_k <= j for L_k in L):
                dp[i][j] = sum((dp[k][i-1] * (1 if U_k <= j else 0)) % mod for k in range(N)) + sum((dp[k][i-1] * (1 if L_k <= j else 0)) % mod for k in range(M))
            elif any(U_k <= j for U_k in U):
                dp[i][j] = sum((dp[k][i-1] * (1 if U_k <= j else 0)) % mod for k in range(N))
            elif any(L_k <= j for L_k in L):
                dp[i][j] = sum((dp[k][i-1] * (1 if L_k <= j else 0)) % mod for k in range(M))
            else:
                dp[i][j] = 0

    return [str(dp[i][j]) for i in range(C + 1)]

T = int(input())

for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    print(*solve(N, M, C, U, L), sep=' ')
