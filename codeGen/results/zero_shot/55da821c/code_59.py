# Read the input
n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

# Sort the plants by their positions
plants.sort(key=lambda p: p[1])

# Initialize a list to store the minimum number of replants for each species
replants = [0] * m

# Iterate over the plants and update the replant count for each species
for i in range(n):
    s, _ = plants[i]
    for j in range(m):
        if s == j + 1:
            replants[j] += 1
            break

# The minimum number of replants is the maximum replant count for any species
min_replants = max(replants)
