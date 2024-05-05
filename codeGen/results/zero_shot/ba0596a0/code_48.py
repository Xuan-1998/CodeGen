def can_cross_stones(stones):
    for i in range(1, len(stones)):
        if abs(stones[i] - stones[i-1]) not in [k-1 for k in range(min(stones), max(stones))]:
            return False
    return True

stones = list(map(int, input().split()))
print(can_cross_stones(stones))
