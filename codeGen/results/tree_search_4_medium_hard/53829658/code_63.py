from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    # Initialize dp dictionary with all values as infinity
    dp = {i: {j: float('inf') for j in range(1, n+1)} for i in range(1, n+1)}

    # Update dp dictionary for each road (si, ti)
    for city, neighbors in graph.items():
        for neighbor in neighbors:
            dp[city][neighbor] = 0
            dp[1][neighbor] += 1

    max_in_degree = max({j: len(graph[j]) for j in range(1, n+1)}.values())

    min_reversed_roads = max_in_degree - 1
    possible_capitals = [city for city, degree in {j: len(graph[j]) for j in range(1, n+1)}.items() if degree == max_in_degree]

    print(min_reversed_roads)
    print(' '.join(map(str, possible_capitals)))

if __name__ == '__main__':
    solve()
