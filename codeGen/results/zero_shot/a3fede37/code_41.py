def max_path_sum(tree):
    max_sum = float('-inf')
    curr_sum = 0

    def dfs(node):
        nonlocal curr_sum, max_sum
        if node < len(tree):  
            left_sum = dfs(2*node+1) if 2*node+1 < len(tree) else -float('inf')
            right_sum = dfs(2*node+2) if 2*node+2 < len(tree) else -float('inf')
            curr_sum += tree[node]
            max_sum = max(max_sum, curr_sum + left_sum + right_sum)
            return curr_sum
        return 0

    dfs(0)

    return max_sum

tree = [int(x) for x in input().split()]
print(max_path_sum(tree))
