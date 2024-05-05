def max_sum_of_path(tree):
    n = len(tree)
    child_map = {}
    
    # Pre-compute the indices of children for each node
    for i in range(n):
        if 2*i+1 < n:
            child_map[i] = 2*i+1
        if 2*i+2 < n:
            child_map[i] = 2*i+2
    
    dp = [0]*n
    max_sum = float('-inf')
    
    # Calculate the maximum sum of a path for each node
    for i in range(n-1, -1, -1):
        if i*2+1 < n:
            left_child = child_map[i*2+1]
            dp[i] = max(dp[left_child], tree[left_child]) + tree[i]
        elif i*2+2 < n:
            right_child = child_map[i*2+2]
            dp[i] = max(dp[right_child], tree[right_child]) + tree[i]
        else:
            if i > 0:
                parent = (i-1)//2
                dp[i] = max(dp[parent], tree[parent]) + tree[i]
        
        # Update the maximum sum
        max_sum = max(max_sum, dp[i])
    
    return max_sum

if __name__ == "__main__":
    n = int(input())
    tree = [int(x) for x in input().split()]
    print(max_sum_of_path(tree))
