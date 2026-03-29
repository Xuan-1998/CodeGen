import sys

# Read input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Initialize dp table with 0s
    dp = [0] * (C + 1)
    dp[0] = 1  # Base case: one way to build a 0-sequence

    for i in range(1, C + 1):
        for j in range(min(i, N), -1, -1):
            if U[j] <= i:
                dp[i] += dp[max(0, i - U[j])]
        for k in range(min(i, M), -1, -1):
            if L[k] <= i:
                dp[i] += dp[max(0, i - L[k])]

    # Print the result
    print(*dp, sep=' ')
