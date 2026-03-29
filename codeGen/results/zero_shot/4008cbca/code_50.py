from collections import deque

def min_inserts(board, hand):
    # Define the transition function
    def insert(board, color):
        new_board = list(board)
        for i in range(len(new_board)):
            if new_board[i] == color:
                new_board.insert(i+1, color)
                break
        return "".join(new_board)

    # Define the goal state
    goal_state = "RRR"  # No more inserts needed

    # Initialize the queue and the visited set
    queue = deque([(board, 0)])  # (board configuration, number of inserts)
    visited = {board: 0}

    while queue:
        current_board, num_inserts = queue.popleft()
        if current_board == goal_state:
            return num_inserts

        for color in hand:
            new_board = insert(current_board, color)
            if new_board not in visited or visited[new_board] > num_inserts + 1:
                visited[new_board] = num_inserts + 1
                queue.append((new_board, num_inserts + 1))

    return -1  # Not possible to remove all balls

# Read input from stdin
board = input().strip()
hand = set(input().strip())

# Print the answer to stdout
print(min_inserts(board, hand))
