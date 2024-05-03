replanted = 0
prev_species = None

for x, s in plants:
    if prev_species != s:
        replanted += 1
    prev_species = s

print(replanted)
