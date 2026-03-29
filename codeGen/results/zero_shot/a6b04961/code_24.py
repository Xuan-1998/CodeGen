import sys
from collections import defaultdict, deque

def find_max_hedgehog_beauty():
    n, m = map(int, input().split())
    
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize variables to keep track of the maximum beauty and the current tail length
    max_beauty = 0
    curr_tail_len = 0
    
    # Perform DFS to find the maximum beauty
    visited = set()
    for node in range(n):
        if node not in visited:
            # Reset variables for each new component
            curr_tail_len = 1
            spine_count = 0
            
            # Use a queue to perform BFS from the current node
            queue = deque([node])
            visited.add(node)
            
            while queue:
                curr_node = queue.popleft()
                
                # Update the current tail length and spine count for this component
                if len(visited) > curr_tail_len:
                    curr_tail_len = len(visited)
                elif len(visited) == curr_tail_len:
                    spine_count += 1
                
                for neighbor in graph[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            
            # Update the maximum beauty
            max_beauty = max(max_beauty, curr_tail_len * spine_count)
    
    print(max_beauty)

find_max_hedgehog_beauty()
