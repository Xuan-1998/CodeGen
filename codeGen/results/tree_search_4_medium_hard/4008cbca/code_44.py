def min_insertions(board, hand):
    n = len(board)
    m = len(hand)

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: when the sequence has 0 or 1 elements
    for i in range(m + 1):
        dp[0][i] = max(i, m - i)

    for i in range(1, n + 1):
        for j in range(min(i, m) + 1):
            if board[i - 1] == hand[m - j]:
                # If the current ball matches with the last ball in hand, 
                # we can remove it immediately (0 moves)
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                # Otherwise, we need to insert a ball of any color at position i
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

    # Find the minimum number of moves needed to remove all balls on the table
    ans = min(dp[n])
    
    return ans if ans != float('inf') else -1

# Read input from stdin
board = input().strip()
hand = input().strip()

print(min_insertions(board, hand))
