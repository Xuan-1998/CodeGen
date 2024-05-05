# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read N and M, the number of rows and columns respectively
    N, M = map(int, input().split())
    
    # Calculate the total sum of the steady table
    total_sum = (N * (N - 1)) // 2 * M
    
    # The total sum cannot be greater than M
    if total_sum > M:
        print(0)
    else:
        # Calculate the possible sums for each row
        possible_sums = [i * M for i in range(1, N + 1)]
        
        # Initialize the count of different steady tables
        count = 0
        
        for i in range(N):
            if total_sum - sum(possible_sums[:i+1]) >= possible_sums[i]:
                count += 1
        
        print(count % (10**9 + 7))
