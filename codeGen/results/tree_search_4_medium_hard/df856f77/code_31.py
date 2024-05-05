def min_operations(A):
    N = len(A)
    dp = {0: 0}

    for i in range(1, N):
        min_ops = float('inf')
        for j in range(i):
            if A[j] < A[i]:
                min_ops = min(min_ops, dp[j] + 1)
        dp[i] = min_ops

    return dp[N-1]

A = [int(x) for x in input().split()]
print(min_operations(A))
