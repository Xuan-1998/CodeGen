def min_sum_binary_matrix(N, M):
    # The minimum sum is the smaller dimension of the matrix since we can only
    # fill a square submatrix of size min(N, M) with 1's in the diagonal.
    return min(N, M)

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().split())
    
    # Calculate and print the minimum sum for the current test case
    print(min_sum_binary_matrix(N, M))
