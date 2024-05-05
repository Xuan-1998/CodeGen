# Initialize variables
current_mana = 0
total_mana = 0

for (appearance, health) in sorted_monsters:
    # Calculate the maximum damage needed for this monster
    max_damage = health
    
    # If we haven't cast a spell yet, or if the current appearance time is different from the previous one,
    # we need to calculate the minimum mana required up to this point.
    if appearance != 1 or (appearance == 1 and current_mana == 0):
        total_mana += max_damage
    
    # Update the current mana
    current_mana = max_damage

print(total_mana)
