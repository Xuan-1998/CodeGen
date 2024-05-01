### Code Starts Here ###

# Read input
n, m = map(int, input().split())

# Create a dictionary to store the minimum number of squares required to tile each rectangle
dp = {}

def min_squares(i, j):
    if (i, j) in dp:
        return dp[(i, j)]

    # Base case: A single column can be tiled with one square
    if i == 0 or j == 0:
        result = 1
    else:
        # Recurrence relation: The minimum number of squares required to tile a rectangle is the minimum of two cases:
        #   1. Taking the minimum number of squares required to tile a smaller rectangle and adding one more square on top or to the side
        #   2. Leaving a gap in one dimension because we can place a single square that covers the entire row or column
        result = min(1 + min_squares(min(i, j)-1, min(i, j)-1), i == 0 and 1 or j == 0 and 1)

    # Store the result in the dictionary for future use
    dp[(i, j)] = result

    return result

# Calculate the minimum number of squares required to tile the given rectangle
result = min_squares(n, m)

### Code Ends Here ###
