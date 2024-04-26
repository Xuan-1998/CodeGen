from collections import deque
import sys

def min_reads_to_understand_book(n, adj_list):
    # Compute in-degrees of all vertices
    in_degree = [0] * n
    for i in range(n):
        for j in adj_list[i]:
            in_degree[j] += 1

    # Initialize queue and add all vertices with in-degree 0
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # Initialize count of visited vertices
    count = 0
    # Perform topological sort and keep track of the level
    level = 0
    while queue:
        level += 1
        # Process all vertices at the current level
        for _ in range(len(queue)):
            u = queue.popleft()
            count += 1
            # Decrease in-degree of all adjacent vertices
            for v in adj_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    # If count doesn't match the number of vertices, there is a cycle
    if count != n:
        return -1
    return level

# Read number of test cases
input_lines = iter(sys.stdin.readlines())
t = int(next(input_lines))

# Process each test case
for _ in range(t):
    n = int(next(input_lines))
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, next(input_lines).split()))
        k = line[0]
        dependencies = line[1:]
        for dep in dependencies:
            adj_list[dep - 1].append(i)  # Convert to 0-based index
    print(min_reads_to_understand_book(n, adj_list))
