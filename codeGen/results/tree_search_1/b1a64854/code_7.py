# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read N and M for the current test case
    N, M = map(int, input().split())
    
    # The minimum sum of values is the smaller of N and M
    # because we can place that many 1s in the matrix, 
    # with each row and each column having exactly one 1.
    min_sum = min(N, M)
    
    # Output the minimum sum for the current test case
    print(min_sum)
