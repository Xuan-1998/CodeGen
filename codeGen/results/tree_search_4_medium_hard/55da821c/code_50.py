# Read input from stdin
n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), x))

# Sort the plants by their species and position
plants.sort()

# Initialize a dictionary to store the count of each species
species_count = {}
for plant in plants:
    species_count[plant[0]] = 0

# Initialize variables to keep track of the current section and its end
current_section = 1
section_end = plants[0][1]

# Iterate over the plants and group them by their species
for i, plant in enumerate(plants):
    if plant[1] > section_end:
        # Start a new section
        current_section += 1
        section_end = plant[1]
    species_count[plant[0]] += 1

# Calculate the minimum number of replantings needed
replanted = 0
for i in range(m-1):
    if species_count[i] > 0 and species_count[i+1] == 0:
        # Need to replant all plants in this section
        replanted += species_count[i]
    elif species_count[i+1] > 0:
        # Need to replant one plant from this section
        replanted += 1

print(replanted)
