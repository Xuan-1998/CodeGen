def can_cross_river(stones):
    if len(stones) < 3:
        return False

    for i in range(1, len(stones)):
        jump_distance = stones[i] - stones[i-1]
        if abs(jump_distance - (stones[i-1] - stones[i-2])) > jump_distance + 1:
            return False

    return True

# Read the input from standard input
n = int(input())
stones = list(map(int, input().split()))

# Print the answer to standard output
print(can_cross_river(stones))
