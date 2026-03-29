# Step 2: Sort and count radii
upper_radii_count = {}
for radius in U:
    if radius not in upper_radii_count:
        upper_radii_count[radius] = 0
    upper_radii_count[radius] += 1

lower_radii_count = {}
for radius in L:
    if radius not in lower_radii_count:
        lower_radii_count[radius] = 0
    lower_radii_count[radius] += 1

# Step 3: Generate all possible X-sequences and count the number of different sequences
x_sequence_count = 1  # Start with one sequence (the empty sequence)
for i in range(1, C + 1):
    x_sequence_count *= (upper_radii_count.get(i, 0) + lower_radii_count.get(i, 0))  # Count the number of possible sequences ending at radius i
print(x_sequence_count % (10**9 + 7))
