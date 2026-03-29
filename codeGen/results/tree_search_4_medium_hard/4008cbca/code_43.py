def minMoves(board, hand):
    n = len(board)
    dp = [-1] * (n + 5)

    dp[0] = 0

    for i in range(n+1):
        for c in hand:
            if c not in board[:i]:
                j = i - 1
                while j >= 0 and board[j] == c:
                    j -= 1
                dp[i] = min(dp[i], dp[j + 1] + (i - j - 1) // 3 * 3 + (i - j - 1) % 3)

    return -1 if dp[-1] == -1 else dp[-1]

if __name__ == "__main__":
    board = input().strip()
    hand = input().strip()
    print(minMoves(board, hand))
