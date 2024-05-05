import sys

board = input().strip()
hand = input().strip()

min_insertions = -1
current_length = len(board)

for ball in hand:
    can_remove = False
    for i in range(current_length):
        # Check if inserting the ball at this position would remove some balls
        can_remove = check_insertion(board[:i] + ball + board[i:], current_length)
        if can_remove:
            break
    if can_remove and min_insertions == -1 or min_insertions > current_length:
        min_insertions = current_length

def check_insertion(row):
    count = 1
    for i in range(1, len(row)):
        if row[i] == row[i - 1]:
            count += 1
        else:
            count = 1
        if count >= 3:
            return True
    return False

print(min_insertions)

