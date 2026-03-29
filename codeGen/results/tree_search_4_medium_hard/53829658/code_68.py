import sys
from collections import defaultdict, deque

def solve():
    n = int(input())
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        in_degree[v] += 1

    capital_city = max(range(1, n + 1), key=lambda x: in_degree[x])
    reversed_roads = sum(in_degree[1:] if i != capital_city else in_degree[i - 1] for i in range(1, n + 1))

    print(reversed_roads)
    print(*range(capital_city, n, capital_city), sep=' ')

if __name__ == "__main__":
    solve()
