code block
import sys

def main():
    n, m = map(int, input().split())
    plants = []
    
    for i in range(n):
        species, x = map(float, sys.stdin.readline().split())
        plants.append((species, x))
        
    # sort the plants by their position
    plants.sort(key=lambda x: x[1])
    
    # create a list to store the total length of each section
    section_lengths = [0] * m
    
    for species, x in plants:
        # find the correct section for this plant
        for i in range(m):
            if section_lengths[i] <= x - (i+1) / 2:
                section_lengths[i] += 1
                break
                
    min_plants_to_replant = sum(section_lengths)
    
    print(min_plants_to_replant)

if __name__ == "__main__":
    main()
