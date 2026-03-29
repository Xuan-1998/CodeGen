def min_operations_to_make_array_strictly_increasing():
    N = int(input())
    A = list(map(int, input().split()))
    j_max = max(A)
    
    dp = [[0] * (j_max + 1) for _ in range(N)]
    
    # Initialize base cases
    for i in range(N):
        if i == 0:
            continue
        dp[i][A[i-1]] = 0
    
    # Fill up the dp table
    for i in range(1, N):
        for j in range(A[i-1]+1, j_max + 1):
            if A[i] <= j:
                dp[i][j] = min(j - A[i], dp[i-1][A[i-1]] + (j - A[i]))
            else:
                dp[i][j] = j - A[i]
    
    # Calculate the final answer
    max_val = max(A)
    return dp[N-1][max_val]

print(min_operations_to_make_array_strictly_increasing())
