from collections import defaultdict
from sys import stdin, stdout

def dfs(node, parent, tree, colors, dp):
    if colors[node - 1] == 'W':
        dp[node][offset] = 1
    else:
        dp[node][-offset] = 1

    for child in tree[node]:
        if child != parent:
            dfs(child, node, tree, colors, dp)
            
            # Combine DP states of the child into the current node
            new_dp = defaultdict(int)
            for b1, ways1 in dp[node].items():
                for b2, ways2 in dp[child].items():
                    new_dp[b1 + b2] += ways1 * ways2
            dp[node] = new_dp

def solve(tree, colors):
    n = len(colors)
    dp = [defaultdict(int) for _ in range(n + 1)]
    global offset
    offset = n  # Offset to handle negative balances
    dfs(1, -1, tree, colors, dp)
    return dp[1][0]  # Number of balanced subtrees rooted at node 1

# Read number of test cases
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    parents = list(map(int, stdin.readline().split()))
    colors = stdin.readline().strip()
    
    # Build the tree
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
    
    # Solve the problem
    result = solve(tree, colors)
    
    # Output the result
    stdout.write(f"{result}\n")
