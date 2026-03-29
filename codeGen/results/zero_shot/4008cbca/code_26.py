# Read the input strings
board = input().strip()
hand = input().strip()

# Initialize an empty list to store the result
result = []

# Iterate over each character in the board string
for i in range(len(board)):
    # Initialize a set to keep track of seen colors
    seen_colors = set()
    
    # Initialize a variable to keep track of the minimum number of balls needed at this position
    min_insertions = 0
    
    # Iterate over the remaining characters in the board string
    for j in range(i, len(board)):
        # Add the current color to the set of seen colors
        seen_colors.add(board[j])
        
        # If we have seen three or more consecutive balls with the same color
        if len(seen_colors) == 1:
            # Increment the minimum number of balls needed at this position
            min_insertions += 1
    
    # Add the minimum number of balls needed at this position to the result list
    result.append(min_insertions)

# Print the result
print(sum(result))
