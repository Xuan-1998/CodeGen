import sys

def solve():
    n = int(sys.stdin.readline())
    edges = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        edges.append((si, ti))

    # Find the capital city that minimizes the number of edges to be reversed
    capital = 1  # Assume the first city is the capital initially
    min_edges = float('inf')
    for i in range(2, n+1):
        reachable = False
        queue = [i]
        while queue:
            city = queue.pop(0)
            if city == capital:
                reachable = True
                break
            for edge in edges:
                if edge[1] == city and edge[0] != capital:
                    queue.append(edge[0])
        if not reachable:
            min_edges = min(min_edges, len(edges) - (i-1))
            capital = i

    # Print the minimum number of edges to be reversed
    print(min_edges)

    # Print all possible ways to choose the capital
    capitals = []
    for i in range(2, n+1):
        reachable = False
        queue = [i]
        while queue:
            city = queue.pop(0)
            if city == capital:
                reachable = True
                break
            for edge in edges:
                if edge[1] == city and edge[0] != capital:
                    queue.append(edge[0])
        if reachable:
            capitals.append(str(i))
    print(' '.join(capitals))

solve()
