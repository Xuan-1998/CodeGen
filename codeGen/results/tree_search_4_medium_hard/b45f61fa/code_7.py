def multiply_matrices(i, j):
    if i == 0 or j == n-1:
        # Base case: single matrix remaining
        return 0

    min_multiplications = float('inf')
    for k in range(i, j):
        left_multiplications = multiply_matrices(i, k)
        right_multiplications = multiply_matrices(k+1, j)

        # Calculate the total number of multiplications for this combination
        total_multiplications = left_multiplications + right_multiplications + p[i-1] * p[k] * p[k+1]

        if total_multiplications < min_multiplications:
            min_multiplications = total_multiplications

    return min_multiplications

n = int(input())
p = [int(x) for x in input().split()]

# Fill the memoization dictionary
memo = {}
for i in range(n):
    for j in range(i, n):
        if (i, j) not in memo:
            memo[(i, j)] = multiply_matrices(i, j)

print(memo[(0, n-1)])
