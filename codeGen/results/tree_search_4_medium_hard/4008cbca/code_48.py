def min_insertions(board, hand):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(board) or j == 0:
            return 0

        # base case: no more balls in hand
        if j == 0 and board[i] != 'W':
            return float('inf')

        ans = float('inf')
        for k in range(j):
            # remove all balls at the current position
            next_i, next_j = i + (k != 0), j - k
            if board[next_i] == 'W' and k > 0:
                ans = min(ans, dp(next_i, next_j) + 1)
            else:
                ans = min(ans, dp(next_i, next_j))
        return ans

    return dp(0, len(hand))

# example usage
board = input().strip()
hand = input().strip()
print(min_insertions(board, hand))
