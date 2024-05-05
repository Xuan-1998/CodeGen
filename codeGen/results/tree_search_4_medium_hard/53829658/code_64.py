from collections import deque

n = int(input())
in_degree = [0] * (n + 1)
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    in_degree[v] += 1

q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
capital_city = q[0]

for i in range(1, n + 1):
    dp[capital_city][i] = 1

while q:
    city = q.popleft()
    for neighbor in range(n + 1):
        if neighbor != city and in_degree[neighbor] > 0:
            in_degree[neighbor] -= 1
            dp[city][neighbor] = min(dp[city][neighbor], dp[city][city] + 1)
            if in_degree[neighbor] == 0:
                q.append(neighbor)

min_reversed_roads = float('inf')
capital_cities = []
for i in range(n):
    if dp[capital_city][i + 1] < min_reversed_roads:
        min_reversed_roads = dp[capital_city][i + 1]
        capital_cities = [str(i + 1)]

print(min_reversed_roads)
print('\n'.join(capital_cities))
