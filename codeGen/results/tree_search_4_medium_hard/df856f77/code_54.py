def min_operations():
    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    for i in range(N):
        prev_increasing_index = 0
        min_ops = float('inf')
        for j in range(1, i + 1):
            if A[j] > A[j - 1]:
                prev_increasing_index = j
                min_ops = min(min_ops, dp[prev_increasing_index - 1] + (j - prev_increasing_index))
        dp[i + 1] = min_ops
    return dp[-1]

print(min_operations())
