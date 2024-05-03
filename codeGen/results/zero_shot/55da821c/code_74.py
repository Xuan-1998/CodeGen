def min_replanted_plants():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((s, x))
    
    left = -1
    right = 0
    current_species = 0
    
    for _, x in plants:
        if _ != current_species:
            right = x
            current_species = _
        elif x > right:
            right = x
    
    return n - (right + 1)

print(min_replanted_plants())
