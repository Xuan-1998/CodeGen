MOD = 998244353

def dfs(node, parent):
    # This function will perform a depth-first search and calculate the number of valid permutations
    # for the subtree rooted at 'node'
    ways = 1
    size = 0
    for child in tree[node]:
        if child == parent:
            continue
        child_ways, child_size = dfs(child, node)
        # Combine the child ways with the current ways
        ways = ways * child_ways * comb(size + child_size, size) % MOD
        size += child_size
    return ways, size + 1

def comb(n, k):
    # This function calculates n choose k modulo MOD
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def precompute_factorials(max_n):
    # This function precomputes the factorials and inverse factorials modulo MOD
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

# Read input
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# Precompute factorials and inverse factorials for combination calculations
fact, inv_fact = precompute_factorials(n)

# Start DFS from node 1 (or any node, since it's a tree)
result, _ = dfs(1, -1)

# Since we can rotate the circle, we divide by n to get the unique arrangements
result = result * inv_fact[n] % MOD

# Output the result
print(result)
