def maxPathSum(tree):
    memo = [[-float('inf')] * 2 for _ in range(len(tree))]
    
    def dfs(node, parent):
        if tree[node] == -1:
            return 0
        
        left_sum = dfs(2*node+1, node) if 2*node+1 < len(tree) else -float('inf')
        right_sum = dfs(2*node+2, node) if 2*node+2 < len(tree) else -float('inf')
        
        memo[node][0] = max(left_sum, right_sum)
        memo[node][1] = tree[node] + left_sum
        
        return memo[node][1]
    
    return dfs(0, None)
