import sys

# Read input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Initialize DP table
    dp = {0: 1}

    for i in range(1, C+1):
        dp[i] = (dp[i-1] + sum(r == i for r in U) + sum(r == i for r in L)) % (10**9 + 7)

    # Print results
    print(*[str(dp[i]) for i in range(C)], sep=' ')
