def min_balls_to_remove(board, hand):
    # Count the number of each color ball in the board
    colors = {'R': 0, 'Y': 0, 'B': 0, 'G': 0, 'W': 0}
    for c in board:
        colors[c] += 1

    # Check if it's possible to remove all balls with the given hand
    if sum(colors.values()) > len(hand):
        return -1

    # Initialize a stack to keep track of the sequence of popped balls
    stack = []

    # Iterate over the board and insert the right number of balls into the stack
    for i, c in enumerate(board):
        while colors[c] > 0:
            stack.append(c)
            if len(stack) < 3:
                break
            for _ in range(3):
                stack.pop()
            if not stack or stack[-1] == c:
                break
            colors[c] -= 1

    # If there are still balls left, it's impossible to remove all the balls
    if len(stack) > 0:
        return -1

    return len(hand)
