import sys
from collections import defaultdict

# Function to perform DFS and update DP states
def dfs(node, parent, tree, colors, dp):
    global balanced_subtrees
    color = 1 if colors[node-1] == 'W' else -1  # White is +1, Black is -1
    dp[node] = defaultdict(int)
    dp[node][color] = 1  # Initialize DP state for current node

    # Iterate over children of the current node
    for child in tree[node]:
        if child == parent:
            continue
        dfs(child, node, tree, colors, dp)
        
        # Combine DP states of child into current node's DP state
        new_dp = defaultdict(int)
        for c1 in dp[node]:
            for c2 in dp[child]:
                new_dp[c1 + c2] += dp[node][c1] * dp[child][c2]
        dp[node] = new_dp

    # Check for balanced subtree at current node
    balanced_subtrees += dp[node][0]

# Read input from stdin
def main():
    global balanced_subtrees
    input_lines = sys.stdin.read().splitlines()
    test_case_idx = 0
    while test_case_idx < len(input_lines):
        n = int(input_lines[test_case_idx])
        parents = list(map(int, input_lines[test_case_idx + 1].split()))
        colors = input_lines[test_case_idx + 2]
        tree = defaultdict(list)
        dp = {}

        # Build the tree
        for i in range(2, n + 1):
            tree[parents[i-2]].append(i)
            tree[i].append(parents[i-2])

        balanced_subtrees = 0
        dfs(1, -1, tree, colors, dp)
        print(balanced_subtrees)

        test_case_idx += 3

if __name__ == "__main__":
    main()
