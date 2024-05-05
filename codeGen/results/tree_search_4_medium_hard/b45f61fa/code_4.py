def matrix_chain_order(p):
    n = len(p) - 1

    # Initialize dp table with zeros
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Fill up the dp table using dynamic programming
    for i in range(1, n+1):
        dp[i][i-1] = 0
    for length in range(2, n+1):
        for i in range(1, n-length+2):
            j = i + length - 1
            min_ops = float('inf')
            for k in range(i, j):
                ops = dp[i][k-1] + p[k-1]*p[k]*dp[k+1][j]
                if ops < min_ops:
                    min_ops = ops
                    split_index = k
            dp[i][j] = min_ops

    # Reconstruct the optimal parenthesization string
    result = ""
    i, j = n-2, n-1
    while i > 0:
        if p[split_index+1]*p[split_index]*dp[split_index+1][j] < p[i]*p[j]*dp[i-1][j]:
            result += "A" + str(i) + "B"
            j = split_index
        else:
            result += "A" + str(i) + "C" + str(j)
            i -= 1
    return result

# Example usage
p = [30, 35, 15]
print(matrix_chain_order(p))
