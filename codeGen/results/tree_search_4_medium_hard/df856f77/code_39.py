===BEGIN CODE===
def solve(A):
    n = len(A)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = min(dp[i], 1 + dp[j])
                
    return dp[-1]

A = list(map(int, input().split()))
print(solve(A))
===END CODE===
