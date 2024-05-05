def min_moves_to_remove_all_balls(board, hand):
    n = len(board)
    dp = {(i, board[:i], h): i + 1 if not h else float('inf') for i in range(n+1) for h in {0} | set(hand)}
    
    for i in range(1, n+1):
        for j in range(i):
            k = 1
            while k <= i and board[j+k-1] == board[j]:
                k += 1
            if k >= 3:
                dp[(i, board[:i], set(hand) - {board[i-1]})] = min(dp.get((j+k-1, board[:j+k-1], set(hand) - {board[i-1]})), 0)
    
    return dp.get((n, board, set()), -1)

import sys
board = input().strip()
hand = input().strip()

print(min_moves_to_remove_all_balls(board, hand))
