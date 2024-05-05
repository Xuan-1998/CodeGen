from collections import deque

def has_path(u, v, k):
    reachable = set()
    
    # BFS to find all reachable vertices within k steps or less
    queue = deque([(u, 0)])
    while queue:
        vertex, distance = queue.popleft()
        
        if distance > k:
            break
        
        if distance == k and vertex != u:  # We've reached the maximum distance but not the starting vertex
            return False
        
        reachable.add(vertex)
        
        for next_vertex in range(2**30):  # Iterate through all vertices
            if (vertex & next_vertex) == next_vertex and next_vertex not in reachable:
                queue.append((next_vertex, distance + 1))
    
    return v in reachable

def main():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print("YES" if has_path(u, v, 29) else "NO")

if __name__ == "__main__":
    main()
