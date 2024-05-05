# Read input
board = input().strip()
hand = input().strip()

# Create a dictionary to store the colors of balls on hand
colors_hand = {"R": 0, "Y": 0, "B": 0, "G": 0, "W": 0}
for color in hand:
    if color in colors_hand:
        colors_hand[color] += 1

# Count the number of balls that can be inserted to remove all the balls on the table
min_insertion = len(board) - 2

print(min_insertion)
