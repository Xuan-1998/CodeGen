# Read the number of monsters
n = int(input())

# Initialize the total mana required
total_mana_required = 0

# Initialize the damage at the previous second
previous_damage = 1

for i in range(n):
    # Read the appearance time and health of the current monster
    k, h = map(int, input().split())
    
    # Calculate the minimum amount of mana required to kill this monster
    while previous_damage < h:
        previous_damage += 1
    
    # Add the damage to the total mana required
    total_mana_required += previous_damage - (previous_damage // 2) if previous_damage % 2 == 0 else previous_damage - (previous_damage // 3)
    
    # Update the previous damage for the next monster
    previous_damage = k + 1

print(total_mana_required)
