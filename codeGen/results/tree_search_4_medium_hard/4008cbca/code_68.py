from collections import defaultdict

def min_moves_to_remove_all_balls():
    board = input().strip()
    hand = list(input().strip())
    n, m = len(board), len(hand)

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    dp[0] = [i for i in range(m + 1)]

    for i in range(1, n + 1):
        prev_hand = defaultdict(int)
        for j in range(i):
            prev_hand[board[j]] += 1
        for k in range(m + 1):
            dp[i][k] = min(dp[i - 1][k], dp[i - 1].index(min(prev_hand.values())) if any(prev_hand.values()) >= 3 else float('inf') + (k > 0))
    return dp[n][m]

print(min_moves_to_remove_all_balls())
