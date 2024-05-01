def minFallingPathSum(A):
    m = len(A)
    memo = {(i, j): float('inf') for i in range(m) for j in range(m)}

    # Base case: memo[(0, j)] = 0 for all j.
    for j in range(m):
        memo[0, j] = 0

    # State expression:
    for i in range(1, m):
        for j in range(m):
            min_val = float('inf')
            for k in range(1, m+1):
                if k != j:
                    min_val = min(min_val, memo[i-1, k-1]*A[0][k-1] + A[i][j])
            memo[i, j] = min_val

    # Find the minimum sum
    min_sum = float('inf')
    for j in range(m):
        if memo[m-1, j] < min_sum:
            min_sum = memo[m-1, j]

    return int(min_sum)
