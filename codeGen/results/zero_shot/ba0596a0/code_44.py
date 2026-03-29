# Step 1: Read input
stones = list(map(int, input().split()))

# Step 2: Initialize variables
can_cross = True
prev_jump = stones[0]

# Step 3: Iterate through each stone
for i in range(1, len(stones)):
    # Calculate the possible jumps for this stone
    jumps = [k-1 for k in range(prev_jump+1, prev_jump+4)]
    
    # Check if the current stone is reachable
    if stones[i] not in jumps:
        can_cross = False
        break
    
    # Update the previous jump
    prev_jump = stones[i]

# Step 4: Print the result
print(can_cross)
