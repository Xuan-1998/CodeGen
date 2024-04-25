def count_square_submatrices_with_ones(matrix, n, m):
    count = 0
    # dp[i][j] will store True if all elements are 1 on and above the main diagonal
    # in the submatrix ending at (i, j) with the top-left corner at (i - k, j - k)
    # for some k >= 0, otherwise False.
    dp = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                # For the first row and first column, we can only form submatrices of size 1
                if i == 0 or j == 0:
                    dp[i][j] = True
                    count += 1
                else:
                    # Check if the submatrix of size k+1 ending at (i, j) is valid
                    # by checking the submatrix of size k ending at (i-1, j-1)
                    if dp[i-1][j-1]:
                        dp[i][j] = True
                        # Check if all elements above the main diagonal are 1
                        for k in range(1, min(i, j) + 1):
                            if matrix[i-k][j] == '0':
                                dp[i][j] = False
                                break
                        # If valid, increment the count
                        if dp[i][j]:
                            count += 1
            else:
                dp[i][j] = False
    return count

# Read input from stdin
n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

# Get the count of valid square submatrices
result = count_square_submatrices_with_ones(matrix, n, m)

# Print the result to stdout
print(result)
