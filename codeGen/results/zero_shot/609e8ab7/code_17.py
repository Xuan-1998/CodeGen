def min_operations(tree_size):
    # Read input from stdin
    n = int(input())
    parents = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for _ in range(n)]

    # Initialize variables to keep track of the number of operations and the current value of each vertex
    ops = 0
    values = [0] * (n + 1)

    def dfs(vertex):
        nonlocal ops
        if values[vertex]:
            return

        # Calculate the new range for this vertex
        new_range = (ranges[vertex][0], ranges[vertex][1])

        # Update the value of this vertex and its ancestors
        while vertex:
            values[vertex] += new_range[0]
            values[vertex] -= new_range[1]
            ops += abs(new_range[0]) + abs(new_range[1])
            vertex = parents[vertex]

    # Traverse the tree from the leaves to the root, updating values and calculating operations as we go
    for i in range(n - 1, 0, -1):
        dfs(i)

    return ops


# Read the number of test cases from stdin
T = int(input())

# Run the solution for each test case
for _ in range(T):
    print(min_operations(int(input())))
