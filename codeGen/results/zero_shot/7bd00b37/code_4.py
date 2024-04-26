MOD = 998244353

def dfs(node, parent):
    # Base case: If the node is a leaf, there's only one permutation.
    if len(tree[node]) == 1 and node != root:
        return 1, 1
    
    total_permutations = 1
    size = 0
    for child in tree[node]:
        if child == parent:
            continue

        # Compute permutations and size for each child's subtree.
        child_permutations, child_size = dfs(child, node)
        total_permutations *= child_permutations
        total_permutations *= factorial[size + child_size] * inverse_factorial[size] * inverse_factorial[child_size]
        total_permutations %= MOD
        size += child_size
    
    return total_permutations, size + 1

def prepare_factorials(n):
    # Precompute factorials and their modular inverses.
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

# Read input
n = int(input())
tree = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# Prepare factorials and their inverses for combination calculations
factorial, inverse_factorial = prepare_factorials(n)

# Choose an arbitrary node as the root
root = 1

# Perform DFS to count valid permutations
permutations, _ = dfs(root, -1)

# Print the result
print(permutations)
