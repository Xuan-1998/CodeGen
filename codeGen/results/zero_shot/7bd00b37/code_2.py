import sys
from collections import defaultdict

MOD = 998244353

# Function to compute factorial and inverse factorial modulo MOD
def precompute_factorials(n):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    return fact, inv_fact

# Function to count the number of ways to arrange nodes on a line
def count_arrangements(u, parent):
    ways = 1
    total_children = 0
    for v in tree[u]:
        if v == parent:
            continue
        child_ways, num_children = count_arrangements(v, u)
        ways = ways * child_ways % MOD
        ways = ways * inv_fact[num_children] % MOD
        total_children += num_children
    ways = ways * fact[total_children] % MOD
    return ways, total_children + 1

# Read input
n = int(sys.stdin.readline())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

# Precompute factorials and inverse factorials
fact, inv_fact = precompute_factorials(n)

# Solve the problem
if n == 2:  # Special case for a tree with 2 nodes
    answer = 1
else:
    root = 1
    answer, _ = count_arrangements(root, -1)
    answer = answer * (n - 1) % MOD

# Print the answer
print(answer)
