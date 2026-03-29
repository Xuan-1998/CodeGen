import sys

def solve(board, hand):
    # Initialize a set to keep track of visited states
    visited = set()

    # Define a function to check if the current state is a goal state
    def is_goal_state():
        return all(c == ' ' for c in board)

    # Define a function to perform one step of insertion and removal
    def one_step_insertion():
        next_board = ''
        for b in board:
            if b != ' ':
                next_board += b
            else:
                next_board += hand[0]
                hand = hand[1:]
        return next_board, hand

    # Define a function to perform one step of removal
    def one_step_removal():
        new_board = ''
        remove_count = 0
        for b in board:
            if b == ' ' or (remove_count > 0 and b != board[board.index(' ')-1]):
                new_board += b
            else:
                remove_count += 1
        return new_board, hand

    # Perform BFS to find the minimum number of steps
    queue = [(board, hand)]
    while queue:
        state = queue.pop(0)
        if is_goal_state():
            return len(state[1])
        for next_state in [one_step_insertion(), one_step_removal()]:
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)

    # If no solution found, return -1
    return -1

# Read input from stdin
board = sys.stdin.readline().strip()
hand = [c for c in sys.stdin.readline().strip()]

# Call the solve function and print the result to stdout
print(solve(board, hand))
