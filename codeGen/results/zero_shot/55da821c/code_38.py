min_replants = 0
for i in range(1, m+1):
    min_replants += sum((count - (i-1)) for j, count in species_counts.items() if j < i) + (species_counts.get(i, 0) - (i-1))

print(min_replants)
