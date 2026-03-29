import sys

board = input().strip()
hand = input().strip()

if board[0] == board[-1]:
    print(-1)
    sys.exit()

while True:
    changed = False
    for i in range(len(board) - 1):
        if board[i] == board[i + 1]:
            hand += board[i]
            board = board[:i] + 'X' + board[i + 1:]
            changed = True
    if not changed:
        break

print(len(hand))
