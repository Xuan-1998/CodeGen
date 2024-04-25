def min_sum_binary_matrix(N, M):
    # The minimum sum is the smaller dimension of the matrix,
    # because that's the maximum number of 1s we can have in a row or column.
    return min(N, M)

# Read the number of test cases
T = int(input().strip())

# Iterate over each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().strip().split())
    
    # Calculate and print the result
    print(min_sum_binary_matrix(N, M))
