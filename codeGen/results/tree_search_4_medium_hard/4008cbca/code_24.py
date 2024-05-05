from collections import deque

def min_moves_to_remove_all_boards(board, hand):
    # Initialize a queue for BFS and add the initial state
    queue = deque([(0, set(), [])])  # (last_ball, balls_in_hand, moves_made)

    visited = {(0, s) for s in {frozenset({}), frozenset({c}) | {c} for c in hand}}

    while queue:
        last_ball, balls_in_hand, moves_made = queue.popleft()

        # If this state has already been processed, skip it
        if (last_ball, balls_in_hand) in visited:
            continue

        visited.add((last_ball, balls_in_hand))

        for i in range(len(board)):
            if board[i] not in hand:  # No need to insert a ball of the same color
                new_balls_in_hand = set(balls_in_hand)
                new_moves_made = list(moves_made)

                # Insert a ball at this position
                new_last_ball = i
                if len(new_balls_in_hand) >= hand.count(board[i]):
                    new_balls_in_hand.discard(board[i])
                    new_moves_made.append(i)

                queue.append((new_last_ball, new_balls_in_hand, new_moves_made))

                # If all balls have been removed, return the number of moves
                if not new_balls_in_hand:
                    return len(new_moves_made)

    return -1  # No possible way to remove all boards

# Read input from stdin and print the answer to stdout
board = list(input())
hand = set(input())

print(min_moves_to_remove_all_boards(board, hand))
