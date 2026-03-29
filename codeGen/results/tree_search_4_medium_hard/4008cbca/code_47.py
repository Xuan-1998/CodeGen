from collections import deque

def min_insertions(board, hand):
    dp = {(i, j): float('inf') for i in range(len(board)) for j in [_]}

    def dfs(state):
        i, j = state
        if i < 0:
            return 0

        if dp[state] != float('inf'):
            return dp[state]

        if board[i-1] == hand[0]:
            dp[state] = 1 + min(dfs((i-2, j)) for k in range(j+1) if k % 3 == 0)
        else:
            dp[state] = 1

        return dp[state]

    res = dfs((len(board), len(hand)))
    return -1 if res == float('inf') else res
