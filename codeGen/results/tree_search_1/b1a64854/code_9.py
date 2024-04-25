def min_sum_binary_matrix(N, M):
    # For a square matrix, the minimum sum is N (diagonal of 1s)
    # For a non-square matrix, the minimum sum is 0
    return N if N == M else 0

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().split())
    
    # Calculate and print the minimum sum for the binary matrix
    print(min_sum_binary_matrix(N, M))
