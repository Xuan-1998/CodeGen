MOD = 998244353

def dfs(node, parent):
    # Initialize the DP for the current node
    dp = [1]
    size = 0
    
    for child in tree[node]:
        if child == parent:
            continue
        # Recursively calculate for the children
        child_dp = dfs(child, node)
        
        # Combine the DP values for the current node and the child
        new_dp = [0] * (size + len(child_dp) + 1)
        for i in range(size + 1):
            for j in range(len(child_dp)):
                new_dp[i + j] += dp[i] * child_dp[j]
                new_dp[i + j] %= MOD
                
        dp = new_dp
        size += len(child_dp)
        
    # Multiply by the number of ways to arrange the children around the node
    for i in range(1, size + 1):
        dp[i] *= i
        dp[i] %= MOD
        
    return dp

# Read input
n = int(input())
tree = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# Perform DFS and DP
dp = dfs(1, -1)
print(dp[1])  # The answer is the number of valid permutations for the root node
