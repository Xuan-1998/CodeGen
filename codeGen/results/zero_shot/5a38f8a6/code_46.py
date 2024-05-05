# Define a function to calculate all perfect squares less than or equal to n
def get_perfect_squares(n):
    perfect_squares = []
    i = 1
    while i * i <= n:
        perfect_squares.append(i * i)
        i += 1
    return perfect_squares

# Read the input from stdin
n = int(input())

# Calculate all perfect squares less than or equal to n
perfect_squares = get_perfect_squares(n)

# Initialize a list to store the minimum number of perfect squares for each value up to n
min_perfect_squares = [float('inf')] * (n + 1)
min_perfect_squares[0] = 0

# Iterate over each perfect square
for perfect_square in perfect_squares:
    # Update the minimum number of perfect squares for each value up to n
    for i in range(perfect_square, n + 1):
        min_perfect_squares[i] = min(min_perfect_squares[i], min_perfect_squares[i - perfect_square] + 1)

# Print the minimum number of perfect squares that add up to n
print(min_perfect_squares[n])
