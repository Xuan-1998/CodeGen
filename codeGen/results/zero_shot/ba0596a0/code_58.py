code:
def can_cross_stones():
    stones = [int(x) for x in input().split()]
    max_jump_distance = 1
    for i in range(1, len(stones)):
        if stones[i] - stones[i-1] > max_jump_distance + 2:
            return False
        max_jump_distance = min(max_jump_distance + 1, stones[i] - stones[i-1])
    return True

print(can_cross_stones())
