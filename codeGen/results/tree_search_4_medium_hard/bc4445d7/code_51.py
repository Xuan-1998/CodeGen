# Define a function to compute the maximum sum of edge weights for a given subtree rooted at node u.
def max_sum(node, memo):
    # Base case: If this is a leaf node (i.e., it has no children), return 0.
    if len(parent[node]) == 1:
        return 0
    
    # Initialize the maximum sum to negative infinity.
    max_sum = float('-inf')
    
    # Iterate over all possible edge labels for this subtree.
    for label in range(1, k + 1):
        # Compute the product of the edge label and the sums of its child subtrees (if they exist).
        prod = label
        for child in parent[node]:
            if child != -1:
                prod *= max_sum(child, memo)
        
        # Update the maximum sum if this product is larger.
        max_sum = max(max_sum, prod)
    
    # Store the result in the memoization table.
    memo[node] = max_sum
    
    return max_sum

# Define a function to backtrack and construct the optimal tree structure.
def backtrack(node, memo):
    # Initialize the maximum sum for this subtree.
    max_sum = memo[node]
    
    # Backtrack to find the optimal edge label and child subtrees.
    for child in parent[node]:
        if child != -1:
            # Find the maximum sum of its child subtree rooted at child.
            max_child_sum = backtrack(child, memo)
            
            # Update the maximum sum if this child subtree has a larger sum.
            max_sum = max(max_sum, max_child_sum * memo[child] + 1)
    
    return max_sum

# Read input from stdin.
n = int(input())
parent = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    parent[u].append(v)
    parent[v].append(u)

m, k = map(int, input().split())
prime_factors = list(map(int, input().split()))

# Initialize the memoization table.
memo = [0] * n

# Compute the maximum sum for each node using dynamic programming with memoization.
for i in range(1, n):
    max_sum(i, memo)

# Backtrack to construct the optimal tree structure.
max_distribution_index = 0
for i in range(n):
    max_sum = backtrack(i, memo)
    max_distribution_index += max_sum

print(max_distribution_index % (10**9 + 7))
