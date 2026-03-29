# Step 1: Read input
T = int(input())  # Number of test cases
tables_count = 0

for _ in range(T):
    N, M = map(int, input().split())
    
    # Step 2: Calculate the maximum sum for each row
    max_sum_row = M
    
    # Step 3: Calculate the number of possible tables for each row
    tables_per_row = min(N - 1, (M + 1) // 2)
    tables_count *= pow(2 * tables_per_row + 1, N - 1)
    
    # Step 4: Calculate the final result modulo 10^9
    result = int(tables_count % 1e9)
