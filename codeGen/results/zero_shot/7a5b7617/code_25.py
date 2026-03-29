# Read input
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # Initialize count of different steady tables
    count = 0

    # Loop through all possible sums for each row
    for sum_row in range(1, min(N, M) + 1):
        # Check if the current table is steady
        if all(sum_row * i <= j for i, j in enumerate(range(M, M - N + 2), start=1)):
            # Increment count of different steady tables
            count += 1

    # Print result modulo 1000000000
    print(count % 1000000000)
