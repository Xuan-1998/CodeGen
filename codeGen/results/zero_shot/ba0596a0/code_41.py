python
def can_cross_stones():
    stones = [int(x) for x in input().split()]
    last_stone = stones[-1]
    
    if len(stones) < 3:
        return False
    
    for i in range(2, len(stones)):
        distance = stones[i] - stones[i-1]
        if (distance != (stones[i-1] - stones[i-2]) + 1) and (distance != (stones[i-1] - stones[i-2])) and (distance != (stones[i-1] - stones[i-2]) - 1):
            return False
    
    return True

if __name__ == "__main__":
    print(can_cross_stones())
