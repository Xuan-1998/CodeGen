from collections import deque

def count_trees(relatives):
    n = len(relatives)
    visited = [False] * n
    tree_count = 0
    
    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            
            while queue:
                node = queue.popleft()
                
                # Traverse the tree by visiting all unvisited nodes connected to the current node
                while node < n and not visited[node]:
                    next_node = relatives.index(node + 1)
                    if next_node != -1 and not visited[next_node]:
                        queue.append(next_node)
                        visited[next_node] = True
                    node += 1
                
            tree_count += 1
    
    return tree_count

n = int(input())
relatives = list(map(int, input().split()))
print(count_trees(relatives))
