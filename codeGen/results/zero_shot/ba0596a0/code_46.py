def can_cross(stones):
    k = stones[1] - stones[0]
    for i in range(2, len(stones)):
        if (stones[i] - stones[i-1]) % k != 0:
            return False
    return True

result = can_cross(stones)
print(result)
