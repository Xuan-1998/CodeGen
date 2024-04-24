from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

# Function to perform DFS and count balanced subtrees
def dfs(node, parent):
    global count_balanced
    # Initialize counts for white and black vertices
    white = black = 0
    if colors[node] == 'W':
        white += 1
    else:
        black += 1

    # This map will store the difference between black and white vertices count
    balance_counter = defaultdict(int)
    balance_counter[black - white] = 1

    # Traverse the children of the current node
    for child in tree[node]:
        if child == parent:
            continue
        child_white, child_black, child_balance_counter = dfs(child, node)

        # Combine results from children
        for balance, freq in child_balance_counter.items():
            # If the subtree rooted at the child is already balanced
            if balance == 0:
                count_balanced += freq
            # If there exists a complementing balance in current node's subtree
            if balance_counter[-balance]:
                count_balanced += balance_counter[-balance] * freq

            # Update balance counter for the current node
            balance_counter[balance + black - white] += freq

        white += child_white
        black += child_black

    # Check if the subtree rooted at the current node is balanced
    if white == black:
        count_balanced += 1

    return white, black, balance_counter

# Read the number of test cases
t = int(input())
for _ in range(t):
    # Read the number of vertices
    n = int(input())
    # Read the parent information and build the tree
    parents = list(map(int, input().split()))
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
        tree[i].append(parents[i - 2])

    # Read the colors of the vertices
    colors = [''] + list(input().strip())

    # Initialize the count of balanced subtrees to 0
    count_balanced = 0

    # Perform DFS starting from the root (vertex 1)
    dfs(1, -1)

    # Output the result
    print(count_balanced)
