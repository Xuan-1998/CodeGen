import sys

def min_edges_to_reversal(cities, roads):
    # Build an adjacency list representation of the graph
    graph = {i: [] for i in cities}
    for si, ti in roads:
        graph[si].append(ti)
    
    # Function to calculate the minimum number of edges that need to be reversed
    def min_reversals(c):
        reversals = 0
        visited = set()
        stack = [c]
        while stack:
            city = stack.pop()
            if city not in visited:
                visited.add(city)
                for neighbor in graph[city]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        reversals += 1
        return reversals
    
    # Calculate the minimum number of edges that need to be reversed for each city
    min_reversal = float('inf')
    capital_cities = []
    for c in cities:
        reversal = min_reversals(c)
        if reversal < min_reversal:
            min_reversal = reversal
            capital_cities = [c]
        elif reversal == min_reversal:
            capital_cities.append(c)
    
    # Print the results
    print(min_reversal)
    for city in capital_cities:
        print(city, end=' ')
    print()
