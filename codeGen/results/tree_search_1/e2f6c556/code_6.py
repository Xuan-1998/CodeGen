from collections import defaultdict, deque
import sys

def find_order(n, graph):
    visited = [False] * (n + 1)
    on_stack = [False] * (n + 1)
    stack = deque()
    
    def dfs(node):
        visited[node] = True
        on_stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False
            elif on_stack[neighbor]:
                # A cycle is detected.
                return False
        stack.appendleft(node)
        on_stack[node] = False
        return True
    
    for i in range(1, n + 1):
        if not visited[i]:
            if not dfs(i):
                return -1, []
    return stack, visited

def count_components(n, graph, visited):
    count = 0
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            dfs(i)
    return count

def main():
    input_lines = list(sys.stdin)
    test_case_idx = 0
    while test_case_idx < len(input_lines):
        n = int(input_lines[test_case_idx].strip())
        graph = defaultdict(list)
        for i in range(1, n + 1):
            line = list(map(int, input_lines[test_case_idx + i].strip().split()))
            for dep in line[1:]:
                graph[dep].append(i)
        test_case_idx += n + 1
        
        order, visited = find_order(n, graph)
        if order == -1:
            print(-1)
        else:
            # Count the number of connected components.
            components = count_components(n, graph, visited)
            print(components)

if __name__ == "__main__":
    main()
