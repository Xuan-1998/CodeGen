# Receive input
n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

# Sort the plants based on their positions
plants.sort(key=lambda x: x[1])

# Initialize a dictionary to store the count of each species
species_count = {}
for s, _ in plants:
    if s not in species_count:
        species_count[s] = 0
    species_count[s] += 1

# Calculate the minimum number of replanting needed
replanted = 0
prev_section = None
for s, (count, _) in sorted(species_count.items()):
    if count > 1 and prev_section != s:
        replanted += count - 1
    prev_section = s

print(replanted)
