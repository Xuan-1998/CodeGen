import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
plants = []
for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

# Initialize sections array with zeros
sections = [0] * m

# Group plants by species and update sections array
for s, x in plants:
    sections[s-1] += 1

# Print the minimum number of replanting required
min_replanting = sum(sections[i] - (i+1) for i in range(m))
print(min_replanting)
