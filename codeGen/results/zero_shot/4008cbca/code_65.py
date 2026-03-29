import sys

board = input().strip()
hand = input().strip()

def can_remove_all():
    board_counts = {}
    hand_counts = {}
    
    for ball in board:
        if ball in board_counts:
            board_counts[ball] += 1
        else:
            board_counts[ball] = 1
    
    for ball in hand:
        if ball in hand_counts:
            hand_counts[ball] += 1
        else:
            hand_counts[ball] = 1
    
    for color, count in board_counts.items():
        if count > 0 and (color not in hand_counts or hand_counts[color] < count):
            return False
    
    return True

def min_balls_needed():
    if not can_remove_all():
        return -1
    
    board_counts = {}
    hand_counts = {}
    
    for ball in board:
        if ball in board_counts:
            board_counts[ball] += 1
        else:
            board_counts[ball] = 1
    
    for ball in hand:
        if ball in hand_counts:
            hand_counts[ball] += 1
        else:
            hand_counts[ball] = 1
    
    min_balls = 0
    for color, count in board_counts.items():
        if count > 0 and (color not in hand_counts or hand_counts[color] < count):
            diff = count - hand_counts.get(color, 0)
            min_balls += max(0, diff // 2) + (diff % 2 != 0)
    
    return min_balls

print(min_balls_needed())
