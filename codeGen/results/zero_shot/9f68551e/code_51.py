# Step 1: Read input
n = int(input())  # Number of monsters
k = list(map(int, input().split()))  # Appearance times of each monster
h = list(map(int, input().split()))  # Health of each monster

# Step 2: Initialize total mana required
total_mana = 0

# Step 3: Iterate through each monster
for i in range(n):
    # Calculate the maximum damage needed to kill this monster
    max_damage = h[i]
    
    # Initialize current mana and current time
    current_mana = 1
    current_time = k[i]
    
    # Iterate backwards from the appearance time of this monster
    for t in range(current_time-1, -1, -1):
        # If there are monsters at previous times, calculate their damage
        if i > 0 and k[i-1] <= t:
            max_damage = max(max_damage, h[i-1])
        
        # Calculate the maximum mana needed to kill this monster up to time t
        if current_time - t >= max_damage:
            total_mana += current_mana + (current_time - t) - 1
            break
        
        # Increase the damage and update the current mana
        current_mana += 1

# Step 4: Print the total mana required
print(total_mana)
