def matrix_chain_order(p):
    n = len(p)
    
    # Create a 2D table dp[][] where entry dp[i][j] represents the minimum number of multiplications needed for matrices p[0..i]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # Reconstruct the optimal parenthesization from the table dp[][].
    # Start with the last pair of parentheses and work backwards.
    sequence = ['' for _ in range(n-1)]
    i, j = n - 2, 0
    while i >= 0:
        if i + 1 < n - 1 and (dp[i][j] > dp[i+1][j]):
            j += 1
        sequence[n-2-i].append(chr(65+j))
        i -= 1
    
    return ''.join(sequence)

p = list(map(int, input().split()))
print(matrix_chain_order(p))
