import sys
from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    max_in_degree = 0
    capital = None
    for city, neighbors in graph.items():
        if len(neighbors) > max_in_degree:
            max_in_degree = len(neighbors)
            capital = city

    reversed_roads = sum(len(neighbors) - 1 for neighbors in graph.values())
    print(reversed_roads)
    print(capital)

if __name__ == "__main__":
    solve()
