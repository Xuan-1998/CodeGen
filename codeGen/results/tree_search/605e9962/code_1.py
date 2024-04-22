from collections import defaultdict
import sys

def count_balanced_subtrees(n, parents, colors):
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
    
    # Initialize the result count
    result = [0]
    
    # Recursive function to calculate DP states
    def dfs(node):
        # DP state: key is the difference between white and black vertices, value is the count
        dp = defaultdict(int)
        dp[0] = 1  # Base case: difference of zero at the current node
        color = 1 if colors[node - 1] == 'W' else -1
        
        for child in tree[node]:
            child_dp = dfs(child)
            new_dp = defaultdict(int)
            
            # Combine DP states of the current node and the child
            for d1 in dp:
                for d2 in child_dp:
                    new_dp[d1 + d2] += dp[d1] * child_dp[d2]
            
            dp = new_dp
        
        # Update the result with balanced subtree counts
        result[0] += dp[color]
        # Adjust the DP state for the current node's color
        new_dp = defaultdict(int)
        for d in dp:
            new_dp[d + color] = dp[d]
        
        return new_dp
    
    # Start DFS from the root
    dfs(1)
    
    # Return the number of balanced subtrees
    return result[0]

# Read the number of test cases
input_data = sys.stdin.read().strip().split('\n')
line_idx = 0
t = int(input_data[line_idx])
line_idx += 1

# Process each test case
for _ in range(t):
    n = int(input_data[line_idx])
    line_idx += 1
    parents = list(map(int, input_data[line_idx].split()))
    line_idx += 1
    colors = input_data[line_idx]
    line_idx += 1
    print(count_balanced_subtrees(n, parents, colors))
