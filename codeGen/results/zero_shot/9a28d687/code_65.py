import sys

n = int(sys.stdin.readline().strip())
costs = list(map(int, sys.stdin.readline().split()))
strings = [sys.stdin.readline().strip() for _ in range(n)]

strings.sort(key=len)

min_cost = 0
current_position = 0

for i in range(1, n):
    if len(strings[i]) < len(strings[i-1]):
        min_cost += costs[current_position]
        current_position = i
    else:
        current_position += 1

min_cost += costs[current_position]

print(min_cost)
