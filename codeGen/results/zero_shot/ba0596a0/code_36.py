# Receive input from stdin
stones = [int(x) for x in input().split()]

# Initialize variables
last_stone_position = stones[-1]
current_stone_position = 0
can_cross_river = True

# Iterate over each stone
for stone_position in stones:
    if current_stone_position + (stone_position - current_stone_position) % 3 != 0:
        can_cross_river = False
        break
    current_stone_position = stone_position

# Print the answer to stdout
print(can_cross_river)
