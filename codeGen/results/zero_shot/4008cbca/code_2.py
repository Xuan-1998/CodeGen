import sys

board = input().strip()
hand = input().strip()

count = 0
current_color = None
consecutive_count = 0

for char in board + hand:
    if char == current_color:
        consecutive_count += 1
    else:
        if current_color is not None and consecutive_count >= 3:
            count += consecutive_count // 3 * (3 - 1) + (consecutive_count % 3 > 0)
        current_color = char
        consecutive_count = 1

if current_color is not None and consecutive_count >= 3:
    count += consecutive_count // 3 * (3 - 1) + (consecutive_count % 3 > 0)

if any(char == char for char in board) or len(hand) < len(set(board)):
    print(-1)
else:
    print(count)
