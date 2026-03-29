===BEGIN CODE===
def solve():
    n = int(input())
    board = input().strip()
    hand = input().strip()

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if len(set(board[:i])) == 1:  # three or more same color balls
            dp[i] = 0
        else:
            min_cost = float('inf')
            for j in range(i):
                if board[j] == board[i - 1]:  # same color as the last ball
                    break
            else:
                j = i - 1
            cost_to_insert = len(hand) - hand.count(board[i - 1])
            dp[i] = min(dp[i - 1], cost_to_insert + (dp[j] if j >= 0 else 0))

    return -1 if dp[n] == float('inf') else dp[n]

print(solve())
