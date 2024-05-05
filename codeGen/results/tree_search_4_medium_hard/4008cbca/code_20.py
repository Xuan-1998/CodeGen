def min_moves_to_remove_all_balls(board, hand):
    n = len(board)
    dp = [[[float('inf')] * 5 for _ in range(n)] for _ in range(2)]

    # Base case: The board is empty with no moves needed.
    for c in range(5):
        if 'RYBGW'[c] in hand:
            hand.remove('RYBGW'[c])
    dp[0][0][c] = 0

    # Fill up the dynamic programming table.
    for i in range(n - 1, -1, -1):
        for prev_c in range(5):
            if board[i] == 'RYBGW'[prev_c]:
                prev_count = count_consecutive_balls(board, i)
                for c in range(5):
                    if 'RYBGW'[c] in hand:
                        new_hand = hand.copy()
                        new_hand.remove('RYBGW'[c])
                        dp[1][i][c] = min(dp[1][i][c], dp[0][i - 1][prev_c] + (not prev_count or not count_consecutive_balls(board, i)))
            else:
                dp[1][i][c] = dp[0][i][c]
    # Find the minimum number of moves needed to remove all balls.
    min_moves = float('inf')
    for c in range(5):
        if 'RYBGW'[c] in hand:
            min_moves = min(min_moves, dp[1][n - 1][c])
    return min_moves if min_moves != float('inf') else -1

def count_consecutive_balls(board, i):
    count = 0
    for c in range(5):
        if board[i] == 'RYBGW'[c]:
            count += 1
        elif count > 2:
            return True
        elif board[i] != 'RYBGW'[c]:
            return False
    return count <= 2

if __name__ == "__main__":
    board = input().strip()
    hand = input().strip()
    print(min_moves_to_remove_all_balls(board, hand))
