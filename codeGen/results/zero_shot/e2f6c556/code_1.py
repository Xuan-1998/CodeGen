from collections import defaultdict, deque
import sys

def find_longest_path(graph, n):
    # Create an array to store the longest path to each node
    longest_path = [0] * (n + 1)
    # Perform a topological sort using Kahn's algorithm
    in_degree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            in_degree[j] += 1
    queue = deque()
    # Enqueue nodes with in-degree 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    # Process nodes in topological order
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            longest_path[v] = max(longest_path[v], longest_path[u] + 1)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    # Check for cycle
    for i in range(1, n + 1):
        if in_degree[i] != 0:
            return -1
    return max(longest_path) + 1

def solve():
    # Read number of test cases
    t = int(sys.stdin.readline())
    for _ in range(t):
        # Read number of chapters
        n = int(sys.stdin.readline())
        graph = defaultdict(list)
        for i in range(1, n + 1):
            # Read dependencies for each chapter
            dependencies = list(map(int, sys.stdin.readline().split()))
            k, required_chapters = dependencies[0], dependencies[1:]
            for chapter in required_chapters:
                graph[chapter].append(i)
        # Find the minimum number of times the book needs to be read
        result = find_longest_path(graph, n)
        print(result)

# Call the solve function to process input and output the result
solve()
