import sys

def solve():
    n, m = map(int, input().split())
    
    # Initialize an empty list for each species
    plants = [[] for _ in range(m)]
    
    # Read the positions of all plants
    for _ in range(n):
        s, x = map(float, sys.stdin.readline().split())
        plants[s-1].append(x)
        
    # Sort the positions of each species in non-decreasing order
    for i in range(m):
        plants[i].sort()
    
    # Initialize the number of replanted plants to 0
    replanted_plants = 0
    
    # Iterate over all sections
    for i, section in enumerate(plants):
        
        # Check if there are any plants in this section
        if not section:
            continue
        
        # For each plant in this section, check how many plants of other species are to its left
        for j, x in enumerate(section):
            
            # Initialize the number of plants of other species to the right
            count = 0
            
            # Iterate over all sections to the left
            for k in range(i):
                
                # Add the number of plants in this section to the count
                count += len(plants[k])
                
            # If there are more plants of other species to the right, we need to replant one plant from this section
            if count > 0:
                replanted_plants += 1
                break
                
    print(replanted_plants)

if __name__ == "__main__":
    solve()
