import sys
from collections import deque

# Read the input from stdin
board = list(input())
hand = list(input())

# Initialize the result variable
result = 0

# Initialize a queue for BFS, with an empty board and no balls used yet
queue = deque([(board[:], 0)])

while queue:
    # Dequeue the next state (board configuration) and the number of balls used so far
    (board_config, num_used_balls) = queue.popleft()

    # If this is the original board configuration, continue with BFS
    if board_config == board:
        continue

    # Initialize a flag to check if all balls have been removed
    all_removed = True

    for i in range(len(board_config)):
        if board_config[i] != ' ':
            # Check if there are three or more consecutive balls of the same color touching
            count_same_color = 1
            j = i + 1
            while j < len(board_config) and board_config[j] == board_config[i]:
                count_same_color += 1
                j += 1

            # If there are not three or more consecutive balls of the same color touching, continue with BFS
            if count_same_color <= 2:
                all_removed = False
                break

    # If all balls have been removed, update the result and stop the BFS
    if all_removed:
        print(result)
        sys.exit(0)

    # Increment the number of balls used for this state
    num_used_balls += 1

    # Add the updated board configuration to the queue
    queue.append((board_config[1:], num_used_balls))

# If no solution was found, output -1
print(-1)
