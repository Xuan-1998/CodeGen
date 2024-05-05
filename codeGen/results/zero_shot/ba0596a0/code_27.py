code
def can_frog_cross(stones):
    max_distance = 0
    for i in range(1, len(stones)):
        if stones[i] - stones[i-1] > max_distance + 2:
            return False
        max_distance = max(max_distance, stones[i] - stones[i-1])
    return True

stones = [int(x) for x in input().split()]
print(can_frog_cross(stones))
