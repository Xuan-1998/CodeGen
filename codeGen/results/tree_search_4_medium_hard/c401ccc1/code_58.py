from collections import deque

def infinite_zoo_queries():
    q = int(input())
    dp = {0: set([0])}
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        # Perform BFS from 0 to find the shortest path to u
        queue = deque([(0, set())])
        visited = set()
        
        while queue:
            node, path = queue.popleft()
            
            if node == u:
                print("YES")
                break
            elif node not in visited:
                visited.add(node)
                
                for neighbor in range(2**30):
                    if node & neighbor and neighbor not in path:
                        queue.append((neighbor, path | {neighbor}))
        
        # If no path is found to u, then it's impossible to reach v from 0
        else:
            print("NO")

infinite_zoo_queries()
