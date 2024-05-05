def min_insertions_to_remove_all_boards(board, hand):
    while True:
        removed = False
        for i in range(len(board) - 2):
            if board[i] == board[i+1] == board[i+2]:
                board = board[:i] + ' ' * 3 + board[i+3:]
                removed = True
                break
        if not removed:
            break
    return len(hand)
