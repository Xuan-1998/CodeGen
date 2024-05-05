from functools import lru_cache

@lru_cache(None)
def can_reach(index, max_reachable_index):
    # Base case: If we've reached the last index, it's possible to reach.
    if index == len(arr) - 1:
        return True
    
    # Calculate the maximum reachable index at this step.
    max_reachable = min(max_reachable_index, index + arr[index])
    
    # Recursively check if it's possible to reach the maximum reachable index.
    return can_reach(max_reachable_index + 1, max_reachable)

arr = [int(x) for x in input().split()]
print(can_reach(0, 0))
