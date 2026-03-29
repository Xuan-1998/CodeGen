def min_insertions(board, hand):
    # Define the colors
    colors = {'R': 0, 'Y': 1, 'B': 2, 'G': 3, 'W': 4}

    # Create a stack to store the colors
    removal_stack = []

    # Initialize the minimum number of insertions required
    min_insertions = 0

    for i in range(len(board)):
        if board[i] in hand:
            # If the current ball is in the hand, remove it from the removal stack
            while len(removal_stack) >= 3 and colors[board[i]] == removal_stack[-1]:
                removal_stack.pop()
            removal_stack.append(colors[board[i]])
        elif removal_stack and colors[board[i]] == removal_stack[-1]:
            # If there are three or more balls of the same color, remove them from the stack
            while len(removal_stack) >= 3 and colors[board[i]] == removal_stack[-1]:
                removal_stack.pop()
        else:
            # If not, push it to the stack
            removal_stack.append(colors[board[i]])

    # Calculate the minimum number of insertions required
    for i in range(len(removal_stack) - 2):
        if removal_stack[i] == removal_stack[i + 1] == removal_stack[i + 2]:
            min_insertions = i
            break

    return min_insertions


# Read input from stdin
board = input().strip()
hand = input().strip()

# Calculate and print the minimum number of insertions required
print(min_insertions(board, hand))
