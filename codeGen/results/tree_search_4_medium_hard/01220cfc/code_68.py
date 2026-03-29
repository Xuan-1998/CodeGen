from collections import defaultdict

def can_reach_last_index(jumps):
    memo = defaultdict(bool)
    
    def dfs(i, reachable):
        if i >= len(jumps) or memo[(i, reachable)]:
            return memo[(i, reachable)]
        
        if i == len(jumps) - 1:  # reached the last index
            return True
        
        reachable_new = reachable or (i + jumps[i] >= len(jumps))
        memo[(i, reachable)] = dfs(i + 1, reachable_new)
        return memo[(i, reachable)]
    
    return dfs(0, False)

# Example usage:
jumps = [2, 3, 1, 1, 4]
print(can_reach_last_index(jumps))  # Output: True
