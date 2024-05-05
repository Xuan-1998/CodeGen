def min_moves_to_remove_all_balls(board, hand):
    memo = {}

    def dfs(board_state, hand_state):
        if (board_state, hand_state) in memo:
            return memo[(board_state, hand_state)]

        if not board_state:  # base case: no more balls in hand
            return 0

        moves_needed = float('inf')

        for ball_color in hand_state:
            new_board_state = list(board_state)
            for i, c in enumerate(new_board_state):
                if c == ball_color:
                    new_board_state[i] = ''
                    break
            else:
                continue
            new_hand_state = set(hand_state) - {ball_color}
            moves_needed = min(moves_needed, 1 + dfs(''.join(new_board_state), new_hand_state))

        memo[(board_state, hand_state)] = moves_needed
        return moves_needed

    board_state = list(board)
    hand_state = set(hand)

    return dfs(board_state, hand_state)
