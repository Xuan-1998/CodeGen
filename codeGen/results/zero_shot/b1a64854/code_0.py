def min_sum_for_binary_matrix(N, M):
    # The minimum sum is the minimum of N and M.
    return min(N, M)

# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().split())
    
    # Calculate and print the minimum sum for the current test case
    print(min_sum_for_binary_matrix(N, M))
