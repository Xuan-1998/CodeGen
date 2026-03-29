import sys

# Input variables
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Initialize dp table with zeros
    dp = [[0] * (C + 1) for _ in range(C + 2)]

    # Base cases: no spheres and sequences longer than C are not possible
    dp[0][j] = 1
    dp[C + 1][j] = 0

    # Calculate dp table using memoization
    for i in range(1, N + 1):
        for j in range(min(C, U[i - 1]), L[0]):
            dp[i][j] = (dp[i][j] + dp[i - 1][min(C, j)]) % (10**9 + 7)

    # Calculate the final answer
    ans = sum(dp[C][j] for j in range(1, C + 1))
    print(ans)
