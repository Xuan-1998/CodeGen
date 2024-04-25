def min_sum_binary_matrix(N, M):
    # If N is not equal to M, the minimum sum is 0.
    # If N equals M, the minimum sum is N (diagonal filled with 1s).
    return N if N == M else 0

# Read the number of test cases from stdin
T = int(input())

# Process each test case
for _ in range(T):
    N, M = map(int, input().split())
    result = min_sum_binary_matrix(N, M)
    print(result)
