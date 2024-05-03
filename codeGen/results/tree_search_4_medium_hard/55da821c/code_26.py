def dp(species_distribution, position):
    memo = {}
    
    def replant_needed(species_distribution, position):
        # Calculate the number of replants needed to achieve the desired distribution
        pass  # You'll need to implement this function
    
    if (species_distribution, position) in memo:
        return memo[(species_distribution, position)]
    
    if all([s == i for s, i in zip(species_distribution, range(1, m+1))]):
        result = 0
    else:
        min_replants = float('inf')
        for next_species in range(m):
            replants_needed_here = replant_needed(species_distribution, position)
            if replants_needed_here == 0:
                break
            species_distribution[position] = next_species
            new_position = position + 1
            result = dp(species_distribution, new_position) + replants_needed_here
            min_replants = min(min_replants, result)
        memo[(species_distribution, position)] = result
    return result

m = int(input())
n = int(input())

# Read the input: species and positions of plants
species_distribution = [0] * n
for i in range(n):
    species, _ = map(int, input().split())
    species_distribution[i] = species - 1  # Adjust indices to match Python's 0-based indexing

print(dp(species_distribution, 0))
