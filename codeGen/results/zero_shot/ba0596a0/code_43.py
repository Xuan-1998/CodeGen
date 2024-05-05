code_block_start
current_position = 0
for position in stones[1:]:
    if abs(position - current_position) not in [1, 2]:
        print("False")
        sys.exit(0)
    current_position = position

print("True")
