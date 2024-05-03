import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

# Sort plants by position
plants.sort(key=lambda p: p[1])

# Initialize section boundaries
section_boundaries = [0] * (m + 1)

# Place each species' plants together in their respective section
for s, x in plants:
    for i in range(1, m + 1):
        if section_boundaries[i - 1] <= x < section_boundaries[i]:
            section_boundaries[i] = x
            break

# Calculate the minimum number of replanting needed
replantings = sum((section_boundaries[i] - section_boundaries[i - 1]) for i in range(1, m + 1)) - n

print(replantings)
