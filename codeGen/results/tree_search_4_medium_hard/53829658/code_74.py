from collections import deque
n = int(input())
in_degrees = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    in_degrees[v] += 1

max_in_degree = max(in_degrees)
capital_cities = [i for i in range(1, n + 1) if in_degrees[i] == max_in_degree]

min_reversed_roads = float('inf')
for capital in capital_cities:
    reversed_roads = 0
    visited = set()
    queue = deque([capital])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor, degree in enumerate(in_degrees):
                if degree > 0 and node == neighbor:
                    degree -= 1
                    if degree > 0:
                        reversed_roads += 1
                    elif neighbor in visited:
                        break
                    queue.append(neighbor)

    min_reversed_roads = min(min_reversed_roads, reversed_roads)

print(min_reversed_roads)
print(capital_cities[0])
