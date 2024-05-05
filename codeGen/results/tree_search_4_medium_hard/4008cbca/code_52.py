from collections import defaultdict

def min_moves_to_remove_balls():
    board, hand = input().split()
    dp = defaultdict(lambda: float('inf'))
    dp[0, 0] = 0
    
    for i in range(len(board)):
        if board[i] in hand:
            for j in range(min(i + 1, len(hand)), -1, -1):
                hand_state = ord(hand[j]) - ord('R')
                dp[(i, hand_state)] = min(dp.get((i, hand_state), float('inf')), dp.get((i-1 if i > 0 else i, hand_state-1), float('inf')) + (hand_state == 0))
    
    return dp.get((len(board), -1), -1)

print(min_moves_to_remove_balls())
