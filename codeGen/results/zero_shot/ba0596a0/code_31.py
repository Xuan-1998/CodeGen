def can_frog_cross(stones):
    for i in range(1, len(stones)):
        # calculate the minimum and maximum possible jumps from the previous stone
        min_jump = stones[i-1] - (stones[i-1] + 2) // 3 * 2
        max_jump = stones[i-1] + (stones[i-1] + 2) // 3 * 2
        
        # check if the frog can jump to the current stone
        if min_jump > stones[i]:
            return False
        
    return True

import sys
stones = [int(x) for x in sys.stdin.readline().split()]
print(can_frog_cross(stones))
