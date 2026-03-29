import sys

def has_path(u, v):
    # Initialize visited set to keep track of visited vertices
    visited = set()
    
    def dfs(current_vertex):
        if current_vertex == v:
            return True  # Found a path!
        if current_vertex in visited:
            return False  # Already visited, no path exists
        visited.add(current_vertex)
        
        # Check all adjacent vertices (u&v=v)
        for next_vertex in range(2**30):
            if u & next_vertex == v and next_vertex not in visited:
                if dfs(next_vertex):
                    return True
        
        return False
    
    return "YES" if dfs(u) else "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(has_path(u, v))
