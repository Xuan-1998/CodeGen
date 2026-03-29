from collections import defaultdict

def can_reach_last_index(arr):
    memo = defaultdict(bool)
    
    def dfs(i):
        if i >= len(arr) - 1:  # reached the last index, return True
            return True
        if memo[i]:  # already computed this state
            return memo[i]
        
        max_reachable_i = i
        for j in range(i + 1, min(i + arr[i] + 1, len(arr))):
            max_reachable_i = max(max_reachable_i, j)
        
        memo[i] = dfs(max_reachable_i) and (max_reachable_i >= len(arr) - 1 or not dfs(max_reachable_i))
        return memo[i]
    
    return dfs(0)

# Example usage:
arr = [2, 3, 1, 1, 4]
print(can_reach_last_index(arr))  # Output: True
