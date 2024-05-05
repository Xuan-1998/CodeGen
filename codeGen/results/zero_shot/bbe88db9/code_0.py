import sys

def solve():
    n = int(sys.stdin.readline())
    p = [int(x) for x in sys.stdin.readline().split()]
    
    # Create a graph with adjacency list representation
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i].append(i-1)
        graph[i].append(p[i-1])
    
    # Perform BFS to find the shortest path
    queue = [n]
    parent = [-1] * (n+1)
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if parent[neighbor] == -1:
                parent[neighbor] = node
                queue.append(neighbor)
    
    # Calculate the number of portal moves needed
    moves = 0
    node = n
    while node != 0:
        node = parent[node]
        moves += 1
    
    print(moves % (10**9 + 7))

if __name__ == "__main__":
    solve()
