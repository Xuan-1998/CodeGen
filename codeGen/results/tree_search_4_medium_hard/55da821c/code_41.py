import sys
from collections import defaultdict

def min_replanted_plants():
    n, m = map(int, input().split())
    plants = [int(input()), float(input())] + [(i, 0.0) for i in range(1, m+1)]
    plants.sort(key=lambda x: x[1])

    memo = defaultdict(lambda: (float('inf'), -1))

    def dp(section, remaining_plants):
        if section == m:
            return 0
        if remaining_plants == 0:
            return float('inf')
        if (section, remaining_plants) in memo:
            return memo[(section, remaining_plants)]
        
        min_replanted = float('inf')
        for i, plant_species in enumerate(plants):
            if plant_species[0] == section or i == 0 or plants[i-1][0] != section:
                new_section = section
                if i > 0 and plants[i-1][0] < section:
                    new_section += 1
                replanted_plants = dp(new_section, remaining_plants-1)[0]
                min_replanted = min(min_replanted, replanted_plants + (section != plant_species[0]))
        
        memo[(section, remaining_plants)] = (min_replanted, section)
        return min_replanted,

    print(dp(1, n)[0])

if __name__ == "__main__":
    min_replanted_plants()
