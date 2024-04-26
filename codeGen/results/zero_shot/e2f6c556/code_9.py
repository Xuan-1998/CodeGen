from collections import defaultdict, deque
import sys

def find_ordering(num_chapters, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * (num_chapters + 1)
    
    # Build the graph and compute indegrees
    for chapter, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph[prereq].append(chapter)
            indegree[chapter] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque([i for i in range(1, num_chapters + 1) if indegree[i] == 0])
    ordering = []
    while queue:
        node = queue.popleft()
        ordering.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if topological ordering is possible
    if len(ordering) != num_chapters:
        return -1

    # Find the longest path in the topological ordering
    longest_path = 1
    path_length = [1] * (num_chapters + 1)
    for node in ordering:
        for neighbor in graph[node]:
            path_length[neighbor] = max(path_length[neighbor], path_length[node] + 1)
            longest_path = max(longest_path, path_length[neighbor])
    
    return longest_path

# Read input and process each test case
def main():
    input_data = sys.stdin.readlines()
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))

    for _ in range(num_test_cases):
        num_chapters = int(next(iterator))
        prerequisites = {}
        for i in range(1, num_chapters + 1):
            line = list(map(int, next(iterator).split()))
            prerequisites[i] = line[1:]
        
        result = find_ordering(num_chapters, prerequisites)
        print(result)

if __name__ == "__main__":
    main()
