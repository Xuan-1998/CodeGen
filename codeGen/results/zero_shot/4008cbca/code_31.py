import sys

board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

result = min_balls_to_insert(board, hand)

print(result)
