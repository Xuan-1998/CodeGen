from collections import defaultdict

def max_sum_of_path(root):
    dp = defaultdict(int)
    
    def dfs(node):
        if node is None:
            return 0
        
        left_max_sum = dfs(node[1])
        right_max_sum = dfs(node[2])
        
        current_max_sum = node[0] + max(left_max_sum, right_max_sum)
        
        dp[node[3]] = max(dp.get(node[3], 0), current_max_sum)
        
        return current_max_sum
    
    root_value, *children, _ = map(int, input().split())
    
    dfs((root_value, *children, ''))
    
    return max(dp.values())

print(max_sum_of_path(0))
