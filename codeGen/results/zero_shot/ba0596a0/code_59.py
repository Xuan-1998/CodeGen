def frog_crosses(stones):
    for i in range(1, len(stones)):
        prev_distance = stones[i - 1] - stones[i - 2]
        current_distance = stones[i] - stones[i - 1]
        
        if abs(current_distance - prev_distance) > (prev_distance + 1):
            return False
    
    return True

stones = list(map(int, input().split()))
print(frog_crosses(stones))
