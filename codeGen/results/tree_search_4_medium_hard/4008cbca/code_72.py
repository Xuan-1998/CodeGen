def min_insertions(board, hand):
    n = len(board)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        if board[i - 1] == 'R':
            opposite = 'Y'
        elif board[i - 1] == 'Y':
            opposite = 'B'
        elif board[i - 1] == 'B':
            opposite = 'G'
        else:
            opposite = 'W'
        
        if hand.count(opposite) >= 3:
            dp[i] = min(dp[i], dp[i - 3])
        elif hand.count(opposite) > 0 and i > 1:
            dp[i] = min(dp[i], 1 + dp[i - 1])
        else:
            dp[i] = dp[i - 1]
    
    if dp[n] == float('inf'):
        return -1
    else:
        return dp[n]

board = input().strip()
hand = input().strip()

print(min_insertions(board, hand))
