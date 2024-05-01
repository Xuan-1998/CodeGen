def min_squares(n, m):
    # Initialize the count of squares
    count = 0
    
    # Calculate the size of the largest square that fits into the rectangle
    max_size = min(n, m)
    
    while max_size > 0:
        if n % max_size == 0 and m % max_size == 0:
            # If we can cover the entire area with this square, count it
            count += (n // max_size) * (m // max_size)
            break
        else:
            # Otherwise, decrease the size of the square by 1
            max_size -= 1
    
    return count

# Read input from stdin
n, m = map(int, input().split())

# Print the answer to stdout
print(min_squares(n, m))
