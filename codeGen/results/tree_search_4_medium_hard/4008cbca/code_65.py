def min_moves_to_remove_all_balls(board, hand):
    n = len(board)
    dp = [(0, True)]  # Initialize DP table with base case

    for i in range(1, n):
        prev_clean_pos = None
        same_color_count = 0

        for j in range(i):  # Check balls from left to right
            if board[j] == board[i]:
                same_color_count += 1
            else:
                break

        if same_color_count > 2:  # If more than two balls of the same color
            prev_clean_pos = dp[i - same_color_count - 1][0] + 1
        elif same_color_count == 2:  # If exactly two balls of the same color
            prev_clean_pos = dp[i - same_color_count - 1][0]
        else:
            prev_clean_pos = dp[i - 1][0]

        if not dp[-1][1]:  # If previous position was clean
            dp.append((prev_clean_pos, False))
        else:  # If previous position was not clean
            dp.append((dp[-1][0], True))

    return min_moves if hand >= dp[-1][0] else -1

def read_input():
    board = input().strip()
    hand = int(input())
    return board, hand

board, hand = read_input()
print(min_moves_to_remove_all_balls(board, hand))
