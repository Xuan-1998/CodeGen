from collections import defaultdict, deque
import sys

def find_min_reads(n, prerequisites):
    # Graph representation
    graph = defaultdict(list)
    in_degree = [0] * n

    # Build the graph and in-degree list
    for i in range(n):
        for prereq in prerequisites[i]:
            graph[prereq].append(i)
            in_degree[i] += 1

    # Queue for vertices with no incoming edges
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    # Perform topological sort and count the number of reads
    read_count = 0
    visited = 0
    while queue:
        next_round = deque()
        while queue:
            chapter = queue.popleft()
            visited += 1
            for next_chapter in graph[chapter]:
                in_degree[next_chapter] -= 1
                if in_degree[next_chapter] == 0:
                    next_round.append(next_chapter)
        queue = next_round
        read_count += 1

    # Check if all chapters were visited
    if visited != n:
        return -1
    return read_count

# Read input and process each test case
input_data = sys.stdin.readlines()
iterator = iter(input_data)
t = int(next(iterator))
for _ in range(t):
    n = int(next(iterator))
    prerequisites = [list(map(int, next(iterator).split()))[1:] for _ in range(n)]
    print(find_min_reads(n, prerequisites))
