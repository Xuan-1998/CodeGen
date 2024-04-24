from collections import defaultdict

# Recursive DFS function to count balanced subtrees
def dfs(node, color, tree, balanced_count):
    # Base case: leaf node
    if not tree[node]:
        return (1, 0) if color[node] == 'W' else (0, 1)
    
    # Initialize counts for the current subtree
    white_count, black_count = (1, 0) if color[node] == 'W' else (0, 1)
    
    # Visit all children
    for child in tree[node]:
        child_white, child_black = dfs(child, color, tree, balanced_count)
        white_count += child_white
        black_count += child_black
    
    # Check if the current subtree is balanced
    if white_count == black_count:
        balanced_count[0] += 1
    
    return white_count, black_count

def count_balanced_subtrees(n, parents, colors):
    # Build the tree using adjacency list representation
    tree = defaultdict(list)
    for i in range(2, n+1):
        tree[parents[i-2]].append(i)
    
    # Counter for balanced subtrees
    balanced_count = [0]
    
    # Start DFS from the root node
    dfs(1, colors, tree, balanced_count)
    
    # Return the count of balanced subtrees
    return balanced_count[0]

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    # Read inputs for each test case
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    colors = [''] + list(input().strip())  # Add a dummy value at index 0 for 1-based indexing
    
    # Count and print the number of balanced subtrees
    print(count_balanced_subtrees(n, parents, colors))
