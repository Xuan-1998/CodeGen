import math

def count_squares(n):
    # Generate perfect square numbers up to n
    perfect_squares = [i**2 for i in range(int(math.sqrt(n)) + 1)]
    
    # Initialize the minimum number of squares and the current sum
    min_squares = float('inf')
    current_sum = 0
    
    # Iterate over the perfect squares in descending order
    for square in sorted(perfect_squares, reverse=True):
        # Check if adding the current square exceeds n or equals n
        while current_sum + square > n and current_sum + square != n:
            current_sum += square
        
        # If we've found a valid combination, update min_squares
        if current_sum == n:
            min_squares = min(min_squares, len(perfect_squares) - perfect_squares.index(square))
    
    return min_squares

# Read the input from stdin
n = int(input())

# Calculate and print the result
print(count_squares(n))
