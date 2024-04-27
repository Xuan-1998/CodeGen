from collections import defaultdict

def count_trees(relatives):
    # Create a graph from the relatives' data
    graph = defaultdict(list)
    for i, parent in enumerate(relatives, 1):
        graph[parent].append(i)

    # Initialize the visited set and the tree count
    visited = set()
    trees = 0

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

    for i in range(1, len(relatives) + 1):
        if i not in visited:
            dfs(i)
            trees += 1

    return trees

# Read input from stdin
n = int(input())
relatives = list(map(int, input().split()))

# Print the output to stdout
print(count_trees(relatives))
