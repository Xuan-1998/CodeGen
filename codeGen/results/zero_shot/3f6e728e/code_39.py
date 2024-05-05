import sys

def count_x_sequences(N, M, U, L):
    dp = [0] * (C + 1)
    dp[0] = 1  # base case: no hemispheres of radius 0 can be used to build an X-sequence

    for i in range(1, C + 1):
        for j in range(N):
            if U[j] >= i:
                dp[i] += dp[i - 1]
        for k in range(M):
            if L[k] >= i:
                dp[i] += dp[i - 1]

    return [dp[i] % (10**9 + 7) for i in range(C + 1)]

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    result = count_x_sequences(N, M, U, L)
    print(*result, sep=' ')
