import heapq

def hedgehog_beaauty():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    # Read edges from stdin
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Find longest path as the initial "tail"
    tail = [0]
    visited = {0}
    heap = [(0, 0)]
    
    while heap:
        length, node = heapq.heappop(heap)
        
        if node not in visited:
            visited.add(node)
            tail.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (length + 1, neighbor))
                    
    # Initialize maximum beauty and the number of spines
    max_beauty = len(tail) * m
    num_spines = 0
    
    # Try to increase the length of the tail by finding a new node that's not in the visited set
    for i in range(1, n+1):
        if i not in visited:
            # Check if we can extend the tail with this new node
            extended_tail = []
            node = i
            while node != 0 and node not in visited:
                extended_tail.append(node)
                node = graph[node][0]
            extended_tail.append(0)  # Add the starting node to the extended tail
            
            if len(extended_tail) > len(tail):
                tail = extended_tail
                max_beauty = len(tail) * m
                num_spines = 0
                
    print(max_beauty)

hedgehog_beaauty()
