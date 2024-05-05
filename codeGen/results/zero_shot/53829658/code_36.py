import networkx as nx

def solve():
    n = int(input())
    G = nx.DiGraph()
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        G.add_edge(u, v)
        
    # Calculate the centroid of the graph (which will be our capital city)
    capital = list(G.nodes)[int(nx.centroid(G).index(max(nx.centroid(G))))]
    
    # Initialize a variable to store the minimum number of reversed roads
    min_reversed_roads = float('inf')
    
    for u in G.nodes:
        if u != capital:
            # Calculate the number of reversed roads required from city u
            reversed_roads = 0
            visited = set()
            queue = [u]
            
            while queue:
                v = queue.pop(0)
                if v not in visited:
                    visited.add(v)
                    
                    for neighbor in G[v]:
                        if neighbor == capital:
                            continue
                        
                        if neighbor not in visited:
                            queue.append(neighbor)
                        else:
                            reversed_roads += 1
            
            # Update the minimum number of reversed roads
            min_reversed_roads = min(min_reversed_roads, reversed_roads)
    
    print(min_reversed_roads)
    
    capital_index = list(G.nodes).index(capital) + 1
    
    for city in range(1, n+1):
        if city != capital_index:
            print(city, end=' ')
    
    print()

if __name__ == "__main__":
    solve()
