def min_insertions_to_remove_balls():
    # Read input from stdin
    board = input().strip()
    hand = list(input().strip())

    # Initialize dynamic programming table
    dp_table = [[0, (0, '')] for _ in range(len(board) + 1)]

    # Iterate over the board from left to right
    for i in range(1, len(board) + 1):
        last_ball = board[i - 1]
        window_length = i

        # Calculate minimum number of moves needed to remove all balls up to this point
        min_moves = dp_table[i - 1][0]

        if hand:
            for color in hand[:]:
                new_window_length = i + len(color)
                new_last_ball = last_ball

                if new_window_length >= 3 and color * 3 == last_ball + color * 2:
                    continue

                # Check if it's possible to remove all balls
                while True:
                    try:
                        j = board.index(color, i - new_window_length)
                        break
                    except ValueError:
                        pass

                if i - j >= 3 and board[j] == last_ball:
                    min_moves += dp_table[i - 1][0]
                    break

        # Update dynamic programming table
        dp_table[i] = [min_moves + (i % 2), (window_length, last_ball)]

    # Return final answer
    return dp_table[-1][0]

# Print output to stdout
print(min_insertions_to_remove_balls())
