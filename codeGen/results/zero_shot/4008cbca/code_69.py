import sys
from itertools import combinations

def can_insert(board, hand):
    for color in set(hand):
        i = -1
        for j in range(len(board)):
            if board[j] == color:
                i = j
                break
        if i != -1:
            count = 0
            for k in range(i+3):
                if board[k] == color and k+i <= len(board) - 1:
                    count += 1
                    if count >= 3:
                        return True
    return False

def main():
    board = input().strip()
    hand = input().strip()
    
    colors = set(hand)
    unique_colors_in_hand = len(colors)
    
    for color in set(board):
        if (board.count(color) + unique_colors_in_hand) >= 3:
            print(-1, file=sys.stderr)
            return
    
    min_inserts = float('inf')
    for r in range(1, len(hand)+1):
        for c in combinations(hand, r):
            new_board = board
            for b in c:
                new_board += b
            if can_insert(new_board, ''.join(set(hand) - set(c))):
                min_inserts = min(min_inserts, len(c))
    
    print(min_inserts)

if __name__ == "__main__":
    main()
