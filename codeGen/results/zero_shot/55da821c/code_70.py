n, m = map(int, input().split())
plants = list(map(lambda x: (int(x.split()[1]), float(x.split()[-1])), [input() for _ in range(n)]))
plants.sort(key=lambda x: x[1])
replanted = 0
current_section = 1
for species, position in plants:
    if species != current_section:
        replanted += 1
        current_section = species
print(replanted)
