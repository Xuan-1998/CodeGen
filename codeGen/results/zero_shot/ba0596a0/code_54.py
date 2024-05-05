def can_cross_stones(stones):
    for i in range(1, len(stones)):
        # Check if there's a gap between two stones
        if stones[i] - stones[i-1] > (stones[i] - stones[i-2]) or (stones[i] - stones[i-1]) % 3 != 0:
            return False
    return True

# Read input from stdin
input_stones = list(map(int, input().split()))

# Print the answer to stdout
print(can_cross_stones(input_stones))
