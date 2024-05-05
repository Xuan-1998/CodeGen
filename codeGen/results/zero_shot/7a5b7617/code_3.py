import sys

def count_steady_tables(N, M):
    # Initialize the result to 0
    result = 0

    # Fill up the table row by row
    for i in range(1, N+1):
        # Calculate the minimum sum of elements in the ith row
        min_sum = max(i-1, 0)
        
        # Calculate the maximum sum of elements in the ith row
        max_sum = min(M, i)

        # For each possible sum, calculate the number of ways to fill up the table
        for j in range(min_sum, max_sum+1):
            # Update the result accordingly
            result += 1

    return result % (10**9 + 7)

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(count_steady_tables(N, M))
