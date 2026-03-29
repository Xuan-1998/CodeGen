def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def solve(tree_nodes, tree_edges, prime_factors):
    # Initialize the dp array with zeros
    dp = [[[0] * (10**5 + 7)] * tree_nodes for _ in range(tree_nodes)]

    def dfs(node, product):
        if product == 1:
            return 0
        for neighbor, edge_label in enumerate(tree_edges[node]):
            label = 1
            for p in prime_factors:
                if p % edge_label:
                    break
                label *= p
            if label * edge_label == product:
                dp[neighbor][node][label] = 1

    # Compute the maximum possible distribution index
    max_distribution_index = 0
    for node in range(tree_nodes):
        for neighbor, edge_label in enumerate(tree_edges[node]):
            dfs(neighbor, tree_nodes - 1)
            if product % edge_label == 0:
                max_distribution_index += sum(dp[i][node] for i in range(tree_nodes) if dp[i][node])

    return max_distribution_index

# Read the input
T = int(input())
for _ in range(T):
    n, edges = [int(x) for x in input().split()]
    tree_edges = [0] * (n + 1)
    for edge in edges:
        u, v = edge
        tree_edges[u] += 1
        tree_edges[v] += 1

    m, k = [int(x) for x in input().split()]
    prime_factors = [int(x) for x in input().split()]

    result = solve(n, tree_edges, prime_factors)
    print(result % (10**9 + 7))
