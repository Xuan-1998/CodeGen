board = ['R', 'Y', 'B', 'G', 'W']
hand = ['R', 'Y']

print(min_moves_to_remove_boards(board, hand))  # Output: 2

board = ['R'] * 20
hand = ['R'] + ['Y'] * 5

print(min_moves_to_remove_boards(board, hand))  # Output: -1
