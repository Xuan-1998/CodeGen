def min_balls(board, hand):
    # Parse input strings
    board_list = list(board)
    hand_set = set(hand)

    # Initialize variables
    curr_color = board_list[0]
    count = 1

    # Iterate over the board string
    for i in range(1, len(board_list)):
        if board_list[i] == curr_color:
            count += 1
        else:
            curr_color = board_list[i]
            count = 1

        # Check for consecutive balls with the same color
        if count >= 3 and board_list[i] == curr_color:
            break

    # Calculate the minimum number of balls needed to be inserted
    min_insertions = len(board_list) - count
    if min_insertions < 0:
        return -1

    # Add the hand set as a set of insertions
    for color in hand_set:
        while True:
            try:
                board_list.insert(3, color)
                break
            except ValueError:
                pass

    return min_insertions

board = input().strip()
hand = input().strip()
print(min_balls(board, hand))
