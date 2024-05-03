n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, x = map(float, input().split())
    plants.append((species, x))

plants.sort(key=lambda x: x[1])

segments = []
species_index = {}
for plant in plants:
    species = plant[0]
    if species not in species_index:
        species_index[species] = [plant[1], None]
    else:
        last_segment = species_index[species][1]
        species_index[species][1] = plant[1]
        segments.append((species, last_segment, plant[1]))

optimal_segments = []
current_segment = 0
for plant in plants:
    species, x = plant
    while current_segment < len(segments) - 1 and species != segments[current_segment][0]:
        current_segment += 1
    optimal_segments.append((species, segments[current_segment][2], None))

replanted = 0
for i in range(len(optimal_segments) - 1):
    if optimal_segments[i][2] != segments[i+1][1]:
        replanted += 1

print(replanted)
