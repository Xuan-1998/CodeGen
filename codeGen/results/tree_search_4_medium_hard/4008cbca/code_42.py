def min_moves_to_remove_all_balls(board, hand):
    # Create a memoization table
    memo = {}

    def dfs(i):
        if i in memo:
            return memo[i]

        if i >= len(board) or not board[i]:
            return -1  # Not possible to remove all balls

        # Base case: No more removable sequence
        if i + 2 <= len(board) and [board[i], board[i+1], board[i+2]].count(board[i]) >= 3:
            return 0  # No moves needed

        min_moves = float('inf')

        for j in range(i, -1, -1):
            if [board[j], board[i], board[i+1]].count(board[j]) >= 3:  # Can remove the ball at position i
                new_board = board[:j] + [''] * (i - j) + board[i+2:]
                moves = dfs(j)
                if moves != -1:
                    min_moves = min(min_moves, moves)

        memo[i] = min_moves if min_moves != float('inf') else -1
        return memo[i]

    # Calculate the minimum number of moves needed to remove all balls
    min_moves = dfs(0)

    print(min_moves)
