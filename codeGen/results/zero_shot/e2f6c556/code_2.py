from collections import defaultdict, deque
import sys

def find_order_and_depth(n, prerequisites):
    # Create a graph and an array to count in-degrees
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    depth = [0] * (n + 1)
    
    # Fill the graph and in-degree array
    for i in range(1, n + 1):
        for prereq in prerequisites[i]:
            graph[prereq].append(i)
            in_degree[i] += 1
    
    # Perform a topological sort using Kahn's algorithm
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            depth[i] = 1  # Depth of starting nodes is 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                depth[neighbor] = depth[node] + 1  # Increment depth for each level
    
    # If there is a node with non-zero in-degree, a cycle exists
    if any(in_degree[1:]):
        return -1
    else:
        return max(depth)

# Read input and process each test case
input_data = sys.stdin.readlines()
current_line = 0

# Number of test cases is not given, so we loop until we've processed all lines
while current_line < len(input_data):
    n = int(input_data[current_line].strip())
    current_line += 1
    prerequisites = defaultdict(list)
    
    for i in range(1, n + 1):
        line = list(map(int, input_data[current_line].strip().split()))
        current_line += 1
        k_i = line[0]
        prerequisites[i] = line[1:]
    
    # Find the minimum number of times the book needs to be read
    result = find_order_and_depth(n, prerequisites)
    print(result)
