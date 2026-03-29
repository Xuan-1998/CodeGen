def min_balls_needed(board, hand):
    def can_remove_all(b):
        colors = {}
        for ball in b:
            if ball in colors:
                colors[ball] += 1
            else:
                colors[ball] = 1
        return all(count >= 3 for count in colors.values())

    min_balls = float('inf')
    for _ in range(len(hand) + 1):
        for i in range(len(board)):
            board.insert(0, hand.pop(0))
            if can_remove_all(board):
                min_balls = min(min_balls, len(hand))
                break
        if can_remove_all(board):
            break
    return -1 if min_balls == float('inf') else min_balls

# Read the input from stdin
board = list(input().strip())
hand = list(input().strip())

# Print the output to stdout
print(min_balls_needed(board, hand))
