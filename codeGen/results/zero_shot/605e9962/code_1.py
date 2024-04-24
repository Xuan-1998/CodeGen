from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    global balanced_subtrees
    # Count the current node's color
    white = 1 if colors[node] == 'W' else 0
    black = 1 - white
    
    for child in tree[node]:
        if child != parent:
            w, b = dfs(child, node)
            white += w
            black += b
    
    # Check if the subtree rooted at this node is balanced
    if white == black:
        balanced_subtrees += 1
    
    return white, black

def solve(n, parents, colors):
    global tree, balanced_subtrees
    balanced_subtrees = 0
    tree = defaultdict(list)

    # Construct the tree using the adjacency list
    for i in range(2, n+1):
        tree[parents[i-2]].append(i)
        tree[i].append(parents[i-2])

    # Perform DFS from the root
    dfs(1, -1)

    return balanced_subtrees

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    colors = ' ' + input().strip()  # Adding a space to make the colors 1-indexed
    result = solve(n, parents, colors)
    print(result)
