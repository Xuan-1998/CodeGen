def matrix_chain_order(p):
    n = len(p) - 1

    # Create a 2D list to store the minimum number of multiplications needed
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Initialize the first row and column with 0s
    for i in range(1, n+1):
        dp[i][i-1] = 0

    # Fill the dp table using dynamic programming
    for L in range(2, n+1):
        for i in range(1, n-L+2):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    # Find the optimal order of multiplying the matrices
    i, j = 1, n-1
    s = []
    while i < j:
        min_split = float('inf')
        split_index = -1
        for k in range(i, j):
            q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
            if q < min_split:
                min_split = q
                split_index = k
        s.append('(')
        s.append(chr(ord('A') + i - 1))
        s.append('*'
               )
        i, j = split_index + 1, j
    s.append(')')
    return ''.join(s)

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
