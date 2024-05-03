import sys

# Initialize variables and constants
n, m = map(int, input().split())
plants = []

# Process the input plants
for _ in range(n):
    s, x = map(float, input().split())
    species_positions[s].append(x)
    plants.append((s, x))

# Sort the positions for each species
for i in range(1, m+1):
    species_positions[i].sort()

# Calculate the minimum number of replantings
replantings = 0
species_positions.sort(key=lambda x: (sum(species_positions[x]) / len(species_positions[x]), x))
for s, positions in species_positions.items():
    median_position = sorted(positions)[len(positions) // 2]
    replanted = sum(1 for p in plants if s == p[0] and abs(p[1] - median_position) <= 10**-6)
    replantings += len(positions) - replanted

# Print the answer
print(replantings)
