# Read input
n, m = map(int, input().split())
plants = []
for i in range(n):
    _, x_i = map(float, input().split())
    plants.append((int(input()), x_i))

# Sort plants by species and then by position
plants.sort(key=lambda x: (x[0], x[1]))

# Initialize minimum replanting count to 0
min_replanting_count = 0

# Iterate over plants in order of their positions
for i, (_, x) in enumerate(plants):
    # If the current plant's species is different from the previous one
    if i > 0 and plants[i-1][0] != plants[i][0]:
        # The minimum replanting count increases by 1 for each border needed
        min_replanting_count += 1

# Print the minimum replanting count
print(min_replanting_count)
