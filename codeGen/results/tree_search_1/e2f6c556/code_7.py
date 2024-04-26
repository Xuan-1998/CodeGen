from collections import defaultdict, deque
import sys

def find_longest_path(graph, in_degree, n):
    # Queue for the topological sort
    queue = deque()
    # Distance array to store the longest path to each node
    distance = [0] * (n + 1)
    
    # Initialize the queue with all nodes having in-degree 0
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            # Decrease the in-degree of the neighbor
            in_degree[neighbor] -= 1
            # Update the distance to the neighbor if a longer path is found
            distance[neighbor] = max(distance[neighbor], distance[current] + 1)
            # If in-degree becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for a cycle (graph is not a DAG)
    for i in range(1, n + 1):
        if in_degree[i] != 0:
            return -1
    
    # Return the length of the longest path
    return max(distance)

def solve_book_chapters():
    # Read the number of test cases
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        # Read the number of chapters
        n = int(sys.stdin.readline().strip())
        # Create a graph and in-degree list
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Read the dependencies of the current chapter
            dependencies = list(map(int, sys.stdin.readline().strip().split()))
            k = dependencies[0]
            # Update the graph and in-degree list
            for dep in dependencies[1:]:
                graph[dep].append(i)
                in_degree[i] += 1
        
        # Find the longest path in the DAG
        result = find_longest_path(graph, in_degree, n)
        print(result)

# Call the function to solve the problem
solve_book_chapters()
