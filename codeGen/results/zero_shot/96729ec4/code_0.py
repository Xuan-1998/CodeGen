def count_square_submatrices_with_ones(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0

    # Step 2: Iterate over all possible top-left corners
    for i in range(n):
        for j in range(m):
            # Step 3: Determine the maximum size of square submatrix
            max_size = min(n - i, m - j)
            for size in range(1, max_size + 1):
                valid = True
                # Step 4: Check if submatrix satisfies the condition
                for k in range(size):
                    for l in range(k, size):
                        if matrix[i + k][j + l] == '0':
                            valid = False
                            break
                    if not valid:
                        break
                # Step 5: Increment count if condition is satisfied
                if valid:
                    count += 1
                else:
                    # No need to check larger sizes if this one failed
                    break

    return count

# Read input from stdin
N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]

# Step 7: Output the count
print(count_square_submatrices_with_ones(A))
