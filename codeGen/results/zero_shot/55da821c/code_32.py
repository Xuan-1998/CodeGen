code
n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, x = map(float, input().split())
    plants.append((species, x))

plants.sort(key=lambda x: x[1])

replants = 0
section_species = [0] * m

for plant in plants:
    if section_species[plant[0]-1] == 0:
        section_species[plant[0]-1] = 1
    else:
        replants += 1

print(replants)
