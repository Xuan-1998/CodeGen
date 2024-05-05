board = [c for c in input().strip()]
hand = [c for c in input().strip()]

insertion_points = [i for i, c in enumerate(board) if c not in ['R', 'Y', 'B', 'G', 'W'] or (i > 0 and board[i-1] == c)]

for i in insertion_points:
    board.insert(i, input().strip()[0])

for i in range(len(board) - 2):
    if board[i] == board[i+1] == board[i+2]:
        board = board[:i] + [''] * 3

print(len(insertion_points))
