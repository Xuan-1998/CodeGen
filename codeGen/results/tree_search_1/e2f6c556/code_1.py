from collections import defaultdict, deque
import sys

def find_min_reads(n, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * n
    for chapter, reqs in dependencies.items():
        for req in reqs:
            graph[req-1].append(chapter-1)
            in_degree[chapter-1] += 1
    
    # Perform topological sort using Kahn's algorithm and track maximum distance
    read_count = [0] * n
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    while queue:
        chapter = queue.popleft()
        for next_chapter in graph[chapter]:
            in_degree[next_chapter] -= 1
            if in_degree[next_chapter] == 0:
                queue.append(next_chapter)
            read_count[next_chapter] = max(read_count[next_chapter], read_count[chapter] + 1)
    
    if any(in_degree):  # Cycle detected
        return -1
    
    return max(read_count) + 1  # +1 because we start counting from 0

# Read input and process test cases
input_data = sys.stdin.readlines()
line_iter = iter(input_data)
t = int(next(line_iter))  # Number of test cases

for _ in range(t):
    n = int(next(line_iter))
    dependencies = {}
    for i in range(1, n+1):
        line = list(map(int, next(line_iter).split()))
        k_i = line[0]
        dependencies[i] = line[1:]
    print(find_min_reads(n, dependencies))
