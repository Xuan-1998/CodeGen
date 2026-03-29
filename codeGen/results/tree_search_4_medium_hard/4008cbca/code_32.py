from collections import deque

def dp(last_ball, hand_colors):
    if not last_ball and not hand_colors:  # base case: empty board and no colors in hand
        return 0
    if len(last_ball) >= 3:  # three or more balls of the same color touching
        new_last_ball = last_ball[1:]
        new_hand_colors = hand_colors - {last_ball[0]}
        return 1 + dp(new_last_ball, new_hand_colors)
    else:
        for color in hand_colors:
            if color == last_ball[-1]:
                break
        new_last_ball = last_ball + [color]
        new_hand_colors = hand_colors - {color}
        return 1 + dp(new_last_ball, new_hand_colors)

def solve(board, hand):
    queue = deque([(board, hand, 0)])  # initialize the queue with the initial state and a depth of 0
    while queue:
        board, hand, depth = queue.popleft()
        if not board:  # base case: empty board
            return depth
        last_ball = board[-1]
        min_depth = float('inf')
        for color in hand:
            if color == last_ball[0]:
                break
        new_board = board[:-1] + [color]
        new_hand = hand - {color}
        queue.append((new_board, new_hand, depth + 1))
    return -1

board = input().strip()
hand = set(input().strip())
print(solve([*board], hand))
