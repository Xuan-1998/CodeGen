def solve():
    # Read input from stdin
    board = input().strip()
    hand = input().strip()

    # Initialize a stack to store balls that can be inserted
    insert_stack = []

    # Iterate over the board and find positions where we can insert balls
    for i in range(len(board)):
        if (i == 0 or board[i-1] != board[i]) and (i == len(board) - 1 or board[i] != board[i+1]):
            insert_stack.append(i)

    # Initialize a variable to store the number of balls that need to be inserted
    num_insert = 0

    # Iterate over the hand and find balls that can be inserted into the board
    for ball in hand:
        while insert_stack and (board[insert_stack[-1]] == ball or len(set([board[i] for i in range(insert_stack[-1]-2, insert_stack[-1]+3)])) < 4):
            insert_stack.pop()
            num_insert += 1

    # If we can still insert balls into the board, return -1
    if insert_stack:
        return -1

    # Return the minimum number of balls that need to be inserted
    return num_insert
