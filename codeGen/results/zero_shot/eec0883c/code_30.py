import sys
from heapq import heapify, heappop

n = int(sys.stdin.readline())
gas_stations = [0] + list(map(int, sys.stdin.readline().split()))
roads = []

for _ in range(n - 1):
    u, v, c = map(int, sys.stdin.readline().split())
    roads.append((c, u, v))

heapify([(0, 1)])  # Start with the first city and no gas

max_gas = 0
while roads:
    c, u, v = heappop(roads)
    if gas_stations[u] + c > max_gas:
        max_gas = gas_stations[u] + c
    gas_stations[v] -= c

print(max_gas)
