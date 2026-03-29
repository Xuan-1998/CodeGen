def min_operations():
    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    
    for i in range(1, N):
        dp[i] = float('inf')
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = min(dp[i], dp[j] + (A[j] != A[i]))
    
    return dp[N] - 1 if dp[N] == float('inf') else dp[N]

print(min_operations())
