n, m = map(int, input().split())
plants = []
for i in range(n):
    s_i, x_i = map(float, input().split())
    plants.append((s_i, x_i))

plants.sort(key=lambda x: x[1])

species_count = {}
for s, x in plants:
    if s not in species_count:
        species_count[s] = 0
    species_count[s] += 1

total_replantings = 0
for species, count in species_count.items():
    if count > 1:
        total_replantings += count - 1

print(total_replantings)
