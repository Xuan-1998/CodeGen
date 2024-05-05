import sys
def can_frog_cross(stones):
    # Check if there are at least 2 stones
    if len(stones) < 2:
        return False

    for i in range(1, len(stones)):
        # Calculate the difference between current and previous stone position
        diff = stones[i] - stones[i-1]
        
        # Check if frog can jump from previous stone to current stone
        if abs(diff - (diff // 2)) > 1:
            return False

    return True

# Read input from stdin
n = int(sys.stdin.readline())
stones = [int(x) for x in sys.stdin.readline().split()]

# Call the function and print the result to stdout
print(can_frog_cross(stones))
