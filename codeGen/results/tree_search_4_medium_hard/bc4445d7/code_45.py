def max_distribution_index(n, edges, k):
    memo = {}

    def dp(node):
        if node not in memo:
            memo[node] = 0
            for child in children[node]:
                memo[node] += dp(child)
        return memo[node]

    # Initialize memo and calculate dp values
    memo = {}
    for node in range(1, n+1):
        children = [child for edge, child in edges if edge[0] == node]
        memo[node] = dp(node)

    # Calculate the maximum possible distribution index
    max_index = 0
    for node in range(1, n+1):
        max_index += memo[node]

    return max_index % (10**9 + 7)
