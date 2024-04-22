from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent, tree, colors, dp):
    # Initialize the DP state for this node based on its color
    dp[node] = (1 if colors[node] == 'W' else 0, 1 if colors[node] == 'B' else 0)
    
    # Iterate over the children of this node
    for child in tree[node]:
        if child != parent:
            # Perform DFS on the child
            dfs(child, node, tree, colors, dp)
            # Combine the DP state of the child with the current node's DP state
            dp[node] = (dp[node][0] + dp[child][0], dp[node][1] + dp[child][1])

def count_balanced_subtrees(tree, colors):
    n = len(tree)
    dp = [None] * n
    result = 0
    
    # Perform DFS from the root (assuming the root is 1)
    dfs(1, -1, tree, colors, dp)
    
    # Count the number of balanced subtrees
    for white, black in dp:
        if white == black:
            result += 1
            
    return result

# Read the number of test cases
num_test_cases = int(input().strip())

# Process each test case
for _ in range(num_test_cases):
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    colors = input().strip()
    
    # Construct the tree
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i-2]].append(i)
        tree[i].append(parents[i-2])
    
    # Count the number of balanced subtrees
    result = count_balanced_subtrees(tree, colors)
    
    # Output the result
    print(result)
