from collections import defaultdict, deque
import sys

# Function to perform topological sort and find the longest path
def min_times_to_read(n, prerequisites):
    # Create a graph and in-degrees count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and in-degree count
    for chapter, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph[prereq].append(chapter)
            in_degree[chapter] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for adj in graph[node]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                queue.append(adj)
    
    # Check for cycle
    if len(topo_order) != n:
        return -1
    
    # Find the longest path
    longest_path = [0] * (n + 1)
    for chapter in topo_order:
        for prereq in graph[chapter]:
            longest_path[prereq] = max(longest_path[prereq], longest_path[chapter] + 1)
    
    return max(longest_path)

# Read input and process test cases
def main():
    input_data = sys.stdin.readlines()
    iterator = iter(input_data)
    t = int(next(iterator))  # Number of test cases
    for _ in range(t):
        n = int(next(iterator))  # Number of chapters
        prerequisites = {}
        for i in range(1, n + 1):
            line = list(map(int, next(iterator).split()))
            prerequisites[i] = line[1:]
        result = min_times_to_read(n, prerequisites)
        print(result)

if __name__ == "__main__":
    main()
