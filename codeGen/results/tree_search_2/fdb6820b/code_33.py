import sys

def solve(m, n, A):
    MOD = 10**9 + 7
    dp = {0: 1}
    for i in range(1, n+1):
        dp[i] = 0
        for j in range(i):
            if A[j] <= i:
                dp[i] += dp.get(i-A[j], 0)
        dp[i] %= MOD
    return dp[n]

m, n = map(int, input().split())
A = list(map(int, input().split()))
print(solve(m, n, A))
