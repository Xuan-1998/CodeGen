# Step 1: Read the input
n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, position = map(float, input().split())
    plants.append((species, position))

# Step 2: Sort the plants by their positions
plants.sort(key=lambda x: x[1])

# Step 3: Initialize a variable to store the minimum number of replanting
replanting = 0

# Step 4: Initialize variables to keep track of the current section and species
current_section = 1
current_species = plants[0][0]

# Step 5: Iterate through the plants
for plant in plants:
    if plant[0] != current_species:
        replanting += 1
        current_section += 1
        current_species = plant[0]

print(replanting)
