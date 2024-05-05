# Read the input list of stones' positions
stones = [int(x) for x in input().split()]

# Initialize the frog's current position and jump distance
frog_pos = 0
k = 1

for stone_pos in stones:
    # Check if the frog can reach the current stone
    while frog_pos + k > stone_pos or frog_pos - k < 0:
        k += 1 if k % 3 == 2 else (1 if k % 3 == 0 else -1)
    
    frog_pos = stone_pos

# Check if the frog reached the last stone
if frog_pos == stones[-1]:
    print(True)  # The frog can reach the last stone
else:
    print(False)  # The frog cannot reach the last stone
