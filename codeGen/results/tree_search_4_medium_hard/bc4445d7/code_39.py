def max_distribution_index(n, parent, k):
    # Initialize the 3D table and fill up the base case (nodes with no children)
    state = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(n)]
    
    def dfs(node, ones):
        if node == n - 1:
            return 0
        
        # Calculate the minimum possible count of ones on the path from the root to this node
        min_ones = (k // pow(parent[node], state[parent[node]][node][1] + 1) + 1)
        
        # Initialize the maximum possible distribution index for this node's subtree
        max_distribution_index = 0
        
        for _ in range(min_ones, k):
            temp_state = [state[node][child][i] for child, i in enumerate(parent)]
            
            if all(temp_state[i - 1] + (ones == i) <= ones for i in range(2, min_ones)):
                max_distribution_index += (min_ones - 1)
                
        return dfs(parent[node], min_ones - 1) + max_distribution_index
    
    # Calculate the maximum possible distribution index of the tree
    return pow(n - 1, k, 10**9 + 7)
