import sys

def can_remove_all_balls(board, hand):
    inserted = 0
    for i in range(len(board)):
        if board[i] == 'R' and (i < len(board) - 2 and board[i:i+3].count('R') >= 3):
            inserted += 1
            continue
        if board[i] == 'Y' and (i < len(board) - 2 and board[i:i+3].count('Y') >= 3):
            inserted += 1
            continue
        if board[i] == 'B' and (i < len(board) - 2 and board[i:i+3].count('B') >= 3):
            inserted += 1
            continue
        if board[i] == 'G' and (i < len(board) - 2 and board[i:i+3].count('G') >= 3):
            inserted += 1
            continue
        if board[i] == 'W' and (i < len(board) - 2 and board[i:i+3].count('W') >= 3):
            inserted += 1
            continue

    remaining_balls = [c for c in board if c != 'R' and c != 'Y' and c != 'B' and c != 'G' and c != 'W']
    return len(remaining_balls) > 0 or -1

def main():
    board = input().strip()
    hand = input().strip()
    result = can_remove_all_balls(board, hand)
    print(result)

if __name__ == "__main__":
    main()
