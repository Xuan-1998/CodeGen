from collections import deque

def min_moves_to_remove_all_balls(board, hand):
    n = len(board)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    q = deque([(0, 0)])
    
    while q:
        i, moves = q.popleft()
        
        if i > 0 and board[i - 1] == board[i]:
            i -= 1
        
        for j in range(i + 1, n + 1):
            if all(board[k] != c for k in range(i, j) if board[k] == c):
                dp[j] = min(dp[j], moves + (j - i > 0))
                q.append((j, dp[j]))
    
    return dp[-1] if hand else -1
