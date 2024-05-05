from collections import deque

def min_moves_to_remove_all_balls(board, hand):
    dp = [[float('inf')] * (len(board) + 1) for _ in range(len(board) + 1)]
    dp[0] = [0] * (len(board) + 1)

    queue = deque([(0, 0)])
    while queue:
        i, j = queue.popleft()
        if i > len(board):
            break
        for k in range(j, min(len(board), j + 3)):
            color = board[k]
            if hand.count(color) >= 3:  # can remove at least 3 balls of the same color
                dp[i][k] = min(dp[i][k], dp[i - 1][j])
        for k in range(j, min(len(board), j + 2)):
            if board[k] == board[j]:  # consecutive balls with the same color
                dp[i][k] = min(dp[i][k], dp[i - 1][j])

    ans = float('inf')
    for i in range(len(board) + 1):
        ans = min(ans, dp[-1][i])
    if ans == float('inf'):
        return -1
    else:
        return ans

# Example usage:
board = input().strip()
hand = input().strip()
print(min_moves_to_remove_all_balls(board, hand))
