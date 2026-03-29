# Define input variables
T = int(input())  # Number of test cases
tables_count = [0] * T  # Initialize count for each test case

for i in range(T):
    N, M = map(int, input().split())  # Read number of rows and columns for each test case
    
    # Calculate the sum of elements in each row
    total_sum = N * (N-1) // 2 * M  # The maximum possible sum for a steady table
    partial_sums = [i*(i+1)//2*M for i in range(1, N+1)]  # Partial sums for each row
    
    # Check if the given constraints satisfy the problem condition
    for j in range(N):
        if partial_sums[j] > M or total_sum - partial_sums[N-1-j] > M:
            tables_count[i] = 0  # No steady table possible, reset count to 0
            break
    else:
        tables_count[i] = pow(2, N*M, 10**9 + 7)  # Calculate the number of different steady tables
    
# Print the counts for each test case
for i in range(T):
    print(tables_count[i])
