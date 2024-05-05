def min_moves(board, hand):
    memo = {}

    def dp(config, count):
        if (config, count) in memo:
            return memo[(config, count)]

        if not config or not count:
            return 0

        moves = float('inf')

        for i, c in enumerate(config):
            if c == 'R' and count >= 1:
                next_config = config[:i] + ['R'] * 3 + config[i+1:]
                next_count = count - 1
                moves = min(moves, dp(next_config, next_count) + 1)
            elif c == 'Y' and count >= 1:
                next_config = config[:i] + ['Y'] * 3 + config[i+1:]
                next_count = count - 1
                moves = min(moves, dp(next_config, next_count) + 1)
            # Add more color combinations here...

        memo[(config, count)] = moves
        return moves

    return dp(board, hand)

# Example usage:
board = input().strip()
hand = input().strip()

print(min_moves(list(board), len(hand)))
