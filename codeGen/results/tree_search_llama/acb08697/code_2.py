import sys

def find_min_stones():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    # Initialize the minimum number of stones as 0 (since we start with at least one stone)
    min_stones = 0
    
    # Iterate through each operation in the sequence
    for op in s:
        if op == '-':  # If the operation is a removal
            min_stones += 1  # We need to have at least one stone after the removal, so increment the minimum number of stones
        else:  # If the operation is an addition
            min_stones -= 1  # The minimum number of stones will decrease by 1 since we're adding a stone
    
    print(min_stones)

find_min_stones()
