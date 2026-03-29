from collections import defaultdict

def max_path_sum(arr):
    memo = defaultdict(int)
    
    def dfs(node, prev_val=0):
        if node < 0:
            return 0
        
        left_sum = max(0, prev_val + arr[node])
        right_sum = max(0, prev_val - arr[node])
        
        if memo[node]:
            return memo[node]
        
        memo[node] = max(left_sum, right_sum)
        return memo[node]
    
    def traverse(node):
        if node < 0:
            return 0
        
        left_sum = dfs(2 * node + 1)  # left child
        right_sum = dfs(2 * node + 2)  # right child
        
        return max(left_sum, right_sum) + arr[node]
    
    return traverse(0)
