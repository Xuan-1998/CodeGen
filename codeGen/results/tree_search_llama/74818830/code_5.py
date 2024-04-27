import math

N = int(input())  # Read N from standard input
count = 0         # Initialize the count of perfect squares

for i in range(1, int(math.sqrt(N)) + 1):
    if (i ** 2) <= N:  # Check if the square is within the range
        count += 1     # Increment the count for each perfect square

print(count)       # Print the result to standard output
