def can_cross(stones):
    n = len(stones)
    dp = {(0, 0): True}
    
    for i in range(1, n):
        for j in range(max(0, stones[i-1]), stones[i]):
            k = (j - stones[i-1]) % 3
            if (k == 0 or k == 2) and dp.get((i-1, k-1), False):
                dp[(i, j - stones[i-1])] = True
            elif k == 1:
                dp[(i, j - stones[i-1])] = dp.get((i-1, k-1), False)
        
        if not any(dp.values()):
            return False
    
    return True

# example usage:
stones = list(map(int, input().split()))
print(can_cross(stones))
