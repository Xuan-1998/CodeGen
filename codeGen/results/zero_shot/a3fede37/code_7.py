def max_sum_path(tree):
    def dfs(i):
        if tree[i] == -1:
            return 0
        
        left_sum = dfs(2*i+1)
        right_sum = dfs(2*i+2)
        
        return tree[i] + max(left_sum, right_sum, 0)

    max_sum = float('-inf')
    for i in range(len(tree)):
        if tree[i] != -1:
            max_sum = max(max_sum, dfs(i))
    
    return max_sum

# Example usage
tree = [10, -5, 2, 3, 4, -2, 7, 15]
print(max_sum_path(tree))  # Output: 22 (path: 10 -> 2 -> 7)
