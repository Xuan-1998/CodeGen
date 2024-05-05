import sys

board = input().strip()
hand = input().strip()

result = min_balls_to_insert(board, hand)
print(result)
