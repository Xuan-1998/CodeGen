import sys

# Read input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Initialize DP array
    dp = [0] * (C + 1)
    dp[0] = 1

    # Calculate transitions for each state
    for i in range(1, C + 1):
        U_i = sum(1 for j in U if j >= i)
        L_i = sum(1 for j in L if j >= i)
        dp[i] = (dp[i-1] * (U_i + L_i)) % (10**9 + 7)

    # Print the result
    print(dp[C])
