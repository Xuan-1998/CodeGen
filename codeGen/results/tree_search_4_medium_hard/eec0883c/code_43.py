import sys

n = int(input())  # number of cities
max_gasoline_per_city = [int(x) for x in input().split()]  # max gasoline per city
roads = []  # list of roads (u, v, c)

for _ in range(n - 1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

dp = {}  # memoization dictionary

def transition(city, gas):
    if city + 1 not in visited:
        for road in roads:
            if road[0] == city and road[2] <= gas:  # check if we can take this road
                return max(dp.get((city, gas - road[2])), gas)
    return dp.get((city, gas), gas)

max_gas = 0

visited = set()

def dfs(city, gas):
    nonlocal max_gas
    visited.add(city)
    for road in roads:
        if road[0] == city and road[1] != city:  # check if we can take this road
            next_city, c = road[1], road[2]
            if next_city not in visited:
                dfs(next_city, min(gas - c, max_gasoline_per_city[next_city]))
    max_gas = max(max_gas, gas)
    return

dfs(0, max_gasoline_per_city[0])

print(max_gas)
