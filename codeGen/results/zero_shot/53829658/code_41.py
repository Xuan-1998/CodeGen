import sys

def find_capital_roads():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        roads.append((si, ti))

    # Create a graph from the roads
    graph = {i: [] for i in range(1, n+1)}
    for si, ti in roads:
        graph[si].append(ti)

    # Find the farthest city from the capital (any city will do)
    capital = max(graph, key=lambda x: len(graph[x]))

    # Count the number of roads to be reversed
    reversed_roads = 0
    for si, ti in roads:
        if ti not in graph[capital]:
            reversed_roads += 1

    # Print the minimum number of roads to be reversed
    print(reversed_roads)

    # Print all possible ways to choose the capital (just one way)
    print([capital])

find_capital_roads()
