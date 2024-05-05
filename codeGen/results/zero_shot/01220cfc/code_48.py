code
import sys

def can_reach_end(jumps):
    curr_index = 0
    max_reachable_index = 0
    
    for jump in jumps:
        if curr_index + jump >= len(jumps) - 1:  # Check if we can reach the end with this jump
            return True
        
        max_reachable_index = max(max_reachable_index, curr_index + jump)
        curr_index += 1
    
    return False

n = int(input())
jumps = list(map(int, input().split()))
print(can_reach_end(jumps))
