import sys
from collections import defaultdict

n, m = map(int, input().split())
species_count_map = defaultdict(int)
section_index = 1

for _ in range(n):
    s_i, x_i = map(float, input().split())
    species_count_map[s_i] += 1
    
    while section_index < s_i:
        # No replanting needed for the first plant
        if section_index == 1:
            break
        
        # Increment the current section index and reset the species count map
        section_index += 1
        species_count_map = defaultdict(int)

    min_replantings = sum(species_count - 1 for species, count in species_count_map.items())
    
    print(min_replantings)
