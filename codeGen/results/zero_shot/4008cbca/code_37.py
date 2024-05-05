for i in range(len(board)):
    for j in range(min(5 - (i // 4), len(hand)), -1, -1):
        new_board = board[:i] + [hand[j]] * (len(hand) - j) + board[i:]
        if can_remove(new_board):
            min_insertions = min(min_insertions, j)
            break
    else:
        continue
    break

def can_remove(board):
    # Check for consecutive same-colored balls and remove them if possible
    i = 0
    while i < len(board) - 2:
        if board[i] == board[i + 1] == board[i + 2]:
            board = board[:i] + [board[i]] * (len(board) - i - 3)
            i -= 1
        else:
            i += 1
    return True if len([ball for ball in set(board)]) <= 4 else False

print(min_insertions) if min_insertions != float('inf') else print(-1)
