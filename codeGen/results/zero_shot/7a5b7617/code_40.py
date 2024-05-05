import sys

# Read input
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    
    # Initialize the number of ways to get the steady table
    ways = 0
    
    # Calculate the total sum that each row should have
    total_sum = (M * (N - 1)) // 2 + M

    # For each possible sum, calculate how many rows it can be divided into and update the number of ways
    for i in range(1, total_sum // N + 1):
        if i <= total_sum % N:
            ways += (total_sum // N) * pow(i, N - 1, 10**9 + 7)
        else:
            ways += pow(i, N, 10**9 + 7)

    # Print the answer
    print(ways % (10**9 + 7))
