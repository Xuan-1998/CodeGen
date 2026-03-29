from collections import defaultdict

def min_operations(A):
    N = len(A)
    dp = [float('inf')] * (N + 1)
    memo = defaultdict(int)

    dp[0] = 0
    for i in range(1, N):
        if A[i] > A[i - 1]:
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = min(dp[i], dp[j] + abs(A[i] - A[j]))
                    memo[dp[i]] = i
                    break
        else:
            dp[i] = dp[i - 1]

    return dp[N - 1]
