def min_reversed_roads(input_file):
    n = int(input().strip())
    
    # Initialize an adjacency list representation of the directed tree.
    adj_list = [[] for _ in range(n+1)]
    
    # Read the roads and build the adjacency list.
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
    
    # Initialize variables to store the minimum reversed roads and capital city.
    min_reversed_roads = float('inf')
    capital_city = None
    
    # Iterate over each city to find the one with the minimum reversed roads.
    for city in range(1, n+1):
        # Perform DFS traversal from this city.
        reversed_roads = dfs(city, adj_list)
        
        # Update the minimum reversed roads and capital city if necessary.
        if reversed_roads < min_reversed_roads:
            min_reversed_roads = reversed_roads
            capital_city = city
    
    # Print the minimum number of roads to be reversed and all possible ways to choose the capital.
    print(min_reversed_roads)
    for i in range(1, n+1):
        if dfs(i, adj_list) == min_reversed_roads:
            print(*range(1, n+1), sep=' ')
            break

def dfs(city, adj_list):
    visited = [False] * (len(adj_list))
    reversed_roads = 0
    
    # Perform DFS traversal from this city.
    stack = [city]
    while stack:
        current_city = stack.pop()
        
        # Update the number of reversed roads if necessary.
        for neighbor in adj_list[current_city]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                reversed_roads += 1
    
    return reversed_roads

if __name__ == "__main__":
    min_reversed_roads(input())
