import sys

def can_remove_all(board):
    for i in range(len(board) - 2):  
        window = board[i:i+3]
        if len(set(window)) == 1:  
            return False
    return True

def min_insertions_to_remove_all(board):
    if not can_remove_all(board):  
        return -1

    min_insertions = 0
    while not can_remove_all(board):  
        for i in range(len(board)):
            new_board = board[:i] + 'R' + board[i:]  
            if can_remove_all(new_board):
                min_insertions += 1
                break
    return min_insertions

board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

print(min_insertions_to_remove_all(board))
