import sys

def find_min_reversed_edges(n, roads):
    graph = [[] for _ in range(n)]
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
    
    min_reversed_edges = 0
    capital_city = 0
    for i in range(n):
        incoming_edges = sum(1 for j in graph[i] if j < i)
        if incoming_edges > min_reversed_edges:
            min_reversed_edges = incoming_edges
            capital_city = i
    
    print(min_reversed_edges)
    
    capital_cities = list(range(n))
    print(*capital_cities, sep='\n')

# Read input from stdin
n = int(sys.stdin.readline())
roads = []
for _ in range(n - 1):
    road = list(map(int, sys.stdin.readline().split()))
    roads.append(road)

find_min_reversed_edges(n, roads)
