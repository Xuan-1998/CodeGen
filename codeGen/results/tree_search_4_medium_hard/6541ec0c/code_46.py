from collections import defaultdict

def xor_tree(n, k, a):
    # Initialize dp table and memoized_function
    dp = [[0] * (k + 1) for _ in range(10**9 + 1)]
    memoized_function = lambda node_val, edge_count: memoize(node_val, edge_count)

    def memoize(node_val, edge_count):
        if dp[node_val][edge_count]:
            return 1
        if node_val < 1 or edge_count <= 0:
            return 0

        for neighbor in get_neighbors(node_val, edge_count):  # assuming you have a function to get neighbors of a node
            if memoize(neighbor[1], edge_count - 1) and xor_values_match(node_val, neighbor[1]):
                return 1

        dp[node_val][edge_count] = 0
        return 0

    def get_neighbors(node_val, edge_count):
        # Your implementation here to get neighbors of a node
        pass

    def xor_values_match(a, b):
        # Your implementation here to check if two values have the same XOR
        pass

    for i in range(n):
        dp[a[i]][k] = 1  # Initialize dp table with YES for every leaf node

    result = []
    for i in range(1, n + 1):  # Traverse tree in reverse order
        if not memoized_function(i, k - i):  # If it's impossible to make all connected components have the same XOR
            result.append("NO")
        else:
            result.append("YES")

    return "\n".join(result)

# Read input from stdin and write output to stdout
input()
print(xor_tree(*map(int, input().split()), *map(int, input().split())))
