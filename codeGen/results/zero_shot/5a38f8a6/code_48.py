import math

def solve(n):
    # Step 1: Create a list of perfect squares
    perfect_squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]

    # Step 2: Sort the list of perfect squares in descending order
    perfect_squares.sort(reverse=True)

    # Step 3: Initialize the minimum number of perfect squares and the current sum
    min_count = 0
    current_sum = 0

    # Step 4: Iterate over the sorted list of perfect squares
    for square in perfect_squares:
        # If adding the current perfect square does not exceed n, add it to the current sum
        while current_sum + square <= n and current_sum < n:
            current_sum += square
            min_count += 1

        # If the current sum exceeds n, break the loop
        if current_sum > n:
            break

    return min_count

# Read input from stdin
n = int(input())

# Print the output to stdout
print(solve(n))
