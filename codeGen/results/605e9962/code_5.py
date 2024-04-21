from collections import defaultdict

def dfs(node, tree, colors, dp):
    color = 1 if colors[node] == 'W' else -1
    dp[node] = defaultdict(int)
    dp[node][color] = 1
    total_balanced_subtrees = 0
    
    for child in tree[node]:
        total_balanced_subtrees += dfs(child, tree, colors, dp)
        
        # Combine child's DP state with the current node's DP state
        new_dp = defaultdict(int)
        for diff in dp[node]:
            for child_diff in dp[child]:
                new_dp[diff + child_diff] += dp[node][diff] * dp[child][child_diff]
        dp[node] = new_dp
    
    # Count the balanced subtrees that include the current node
    total_balanced_subtrees += dp[node][0]
    return total_balanced_subtrees

def solve(n, parents, colors):
    tree = defaultdict(list)
    dp = [{} for _ in range(n + 1)]
    
    # Construct the tree
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
    
    # Start DFS from the root node
    return dfs(1, tree, colors, dp)

# Read the number of test cases
num_tests = int(input())

# Process each test case
for _ in range(num_tests):
    n = int(input())
    parents = list(map(int, input().split()))
    colors = ' ' + input().strip()  # Prepend a space to make the colors 1-indexed
    result = solve(n, parents, colors)
    print(result)
