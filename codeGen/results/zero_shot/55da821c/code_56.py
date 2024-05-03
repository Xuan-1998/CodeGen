import sys

n, m = map(int, sys.stdin.readline().split())
species_count = [0] * (m + 1)
section_plants = [[] for _ in range(m + 1)]
replants = 0

for _ in range(n):
    s_i, x_i = map(float, sys.stdin.readline().split())
    species_count[s_i] += 1
    section_plants[s_i].append(x_i)

for i in range(1, m + 1):
    max_x = max(section_plants[i])
    min_x = min(section_plants[i])
    replants += max_x - min_x

print(replants)
