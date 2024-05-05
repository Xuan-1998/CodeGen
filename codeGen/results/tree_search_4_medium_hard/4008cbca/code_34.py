def min_operations(board, hand):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(board):
            return 0

        res = float('inf')

        for color in set(hand):
            count = 0
            for c in board[i:]:
                if c == color:
                    count += 1
                else:
                    break
            if count >= 3:
                res = min(res, dp(i + count, j) + count)

        memo[(i, j)] = res

        return res

    return -1 if dp(0, 0) == float('inf') else dp(0, 0)
