from collections import defaultdict

# Step 3: DFS Traversal to count balanced subtrees
def dfs(node, graph, colors, balanced_count):
    # White vertices will be counted as 1, black as -1
    color_count = 1 if colors[node] == 'W' else -1
    for child in graph[node]:
        child_count = dfs(child, graph, colors, balanced_count)
        color_count += child_count
    # If the count is zero, we have a balanced subtree
    if color_count == 0:
        balanced_count[0] += 1
    return color_count

def count_balanced_subtrees(n, parents, colors):
    # Step 2: Build Tree
    graph = defaultdict(list)
    for i in range(2, n + 1):
        graph[parents[i - 2]].append(i)

    balanced_count = [0]  # Using a list to pass by reference
    # Step 3: Perform DFS starting from the root (vertex 1)
    dfs(1, graph, colors, balanced_count)
    
    # Step 6: Output the result
    return balanced_count[0]

def main():
    # Read number of test cases
    t = int(input())
    for _ in range(t):
        # Step 1: Parse Input
        n = int(input())
        parents = list(map(int, input().split()))
        colors = ' ' + input().strip()  # Add a space to align indices with 1-based indexing

        # Output the result for each test case
        print(count_balanced_subtrees(n, parents, colors))

if __name__ == "__main__":
    main()
