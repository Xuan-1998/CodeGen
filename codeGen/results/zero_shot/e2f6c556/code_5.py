from collections import defaultdict, deque

def find_longest_path(graph, in_degree, n):
    # Initialize distances to all vertices as 0 and create a queue for topological sort
    distance = [0] * (n + 1)
    queue = deque()

    # Enqueue vertices with in-degree 0 (no dependencies)
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # Process vertices in topological order
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            # Update distance to the current node
            distance[neighbor] = max(distance[neighbor], distance[node] + 1)

    # The minimum number of times to read the book is the max distance
    return max(distance)

def has_cycle(graph, n):
    visited = [False] * (n + 1)
    rec_stack = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[node] = False
        return False

    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i):
                return True
    return False

def solve_book_chapters():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the number of chapters
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        # Read the dependencies and construct the graph
        for i in range(1, n + 1):
            dependencies = list(map(int, input().split()))
            for dep in dependencies[1:]:
                graph[dep].append(i)
                in_degree[i] += 1

        # Check for cycles in the graph
        if has_cycle(graph, n):
            print(-1)
        else:
            # Find the longest path in the graph
            result = find_longest_path(graph, in_degree, n)
            print(result)

# Call the function to solve the problem
solve_book_chapters()
