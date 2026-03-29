import sys

def check_remove(board):
    while True:
        removed = False
        for i in range(len(board) - 2):
            if board[i] == board[i+1] == board[i+2]:
                board = board[:i] + [''] * 3 + board[i+3:]
                removed = True
        if not removed:
            break
    return len([x for x in board if x])

def main():
    board = input().strip()
    hand = input().strip()

    min_insertions = -1
    for i in range(len(hand) + 1):
        new_board = board + [hand[j] for j in range(min(i, len(hand)))]
        if check_remove(new_board) == 0:
            min_insertions = i
            break

    print(min_insertions)

if __name__ == "__main__":
    main()
