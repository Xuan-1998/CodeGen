def can_reach_last_index(jumps):
    farthest_reachable_index = 0
    for i in range(len(jumps)):
        max_reachable_index = i + jumps[i]
        if max_reachable_index > farthest_reachable_index:
            farthest_reachable_index = max_reachable_index
    return farthest_reachable_index == len(jumps) - 1

# Test the function
jumps = [2,3,1,1,4]
print(can_reach_last_index(jumps))  # Output: True
