from collections import defaultdict, deque
import sys

def find_min_reads(n, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    depth = [1] * (n + 1)
    
    # Build the graph and compute in-degrees
    for chapter, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph[prereq].append(chapter)
            in_degree[chapter] += 1
    
    # Queue for nodes with in-degree 0 (i.e., no prerequisites)
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    
    # Topological sort and compute depths
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            depth[neighbor] = max(depth[neighbor], depth[node] + 1)
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If all nodes are not visited, there is a cycle
    if any(in_degree[1:]):
        return -1
    
    # The minimum number of reads is the maximum depth
    return max(depth)

# Read input and process each test case
input_lines = sys.stdin.readlines()
line_index = 0

while line_index < len(input_lines):
    n = int(input_lines[line_index].strip())
    line_index += 1
    prerequisites = {}
    
    for i in range(1, n + 1):
        line = list(map(int, input_lines[line_index].strip().split()))
        line_index += 1
        prerequisites[i] = line[1:]
    
    print(find_min_reads(n, prerequisites))
