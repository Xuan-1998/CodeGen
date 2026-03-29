from collections import defaultdict

def min_moves_to_remove_boards(board, hand):
    dp = [(0, True)]  # base case: no moves needed to remove all balls at position 0 (clean)
    for i in range(len(board)):
        if board[i] == 'R':  # assume 'R' is the color of interest
            clean = False
            min_moves = float('inf')
            for j in range(i + 1):
                if dp[j][1]:  # if position j is clean
                    if i - j >= 2:  # and we have at least three consecutive 'R' balls
                        min_moves = min(min_moves, dp[j][0] + (i - j) // 3)
                        break
            dp.append((min_moves, clean))
        else:
            dp.append((dp[i-1][0] + 1, False))  # not clean; need to insert one more ball

    return dp[-1][0] if dp[-1][1] else -1

# Test your solution
board = input()
hand = input()
print(min_moves_to_remove_boards(board, hand))
