import sys

# Read input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Initialize dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Fill dp array
    for i in range(N):
        for j in range(M):
            if U[i] >= L[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j]

    # Print output
    print(*[dp[i][M] % (10**9 + 7) for i in range(C)], sep=' ')
