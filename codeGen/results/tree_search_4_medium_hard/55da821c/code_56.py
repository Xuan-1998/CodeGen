import sys
from collections import defaultdict

def min_replanting(n, m):
    species_count_map = defaultdict(int)
    last_section_species = None
    
    for _ in range(n):
        s_i, x_i = map(int, input().split())
        
        if not species_count_map[s_i]:
            if last_section_species == s_i:
                section_index += 1
                species_count_map = defaultdict(int)
            last_section_species = s_i
            
        species_count_map[s_i] += 1
    
    return sum(count for count in species_count_map.values())

n, m = map(int, input().split())
print(min_replanting(n, m))
