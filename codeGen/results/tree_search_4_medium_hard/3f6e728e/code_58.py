import sys

# Read input
T = int(input())
mod = 10**9 + 7
dp = [0] * (C+1)
dp[0] = 1  # base case: no sphere

for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    for i in range(C+1):
        dp[i] = (dp[i-1] if i > 0 else 1) * sum((1 if j == i else dp[j]) for j in U)
        dp[i] += sum((1 if k != i else 0) * dp[k] for k in L)
        dp[i] %= mod

    print(' '.join(map(str, dp)))
