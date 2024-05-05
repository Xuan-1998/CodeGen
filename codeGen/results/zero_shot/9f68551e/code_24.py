# Step 1: Read input
n = int(input())  # number of monsters
appearances = list(map(int, input().split()))  # appearance times of each monster
healths = list(map(int, input().split()))  # healths of each monster

# Step 2: Sort the appearances and healths by their order
sorted_appearances = sorted(zip(appearances, healths), key=lambda x: x[0])

# Step 3: Initialize a variable to keep track of the maximum mana used so far
max_mana_used = 0

# Step 4: Iterate over each monster's appearance and health
for i in range(len(sorted_appearances)):
    # Get the current monster's appearance and health
    appearance, health = sorted_appearances[i]
    
    # Calculate the mana required to kill this monster
    # The idea is that we need at least as much mana as the monster's health to kill it
    # We also need some extra mana in case we need to cast multiple spells before killing the monster
    mana_required = max(health, appearance - 1)
    
    # Update our running total of maximum mana used
    max_mana_used = max(max_mana_used, mana_required)

print(max_mana_used)
