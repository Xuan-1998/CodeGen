# Initialize the total mana required
total_mana = 0

# Iterate through the monsters
for i in range(n):
    # Find the earliest monster with health greater than or equal to the current monster's health
    for j in range(i, n):
        if h_j >= h_i:
            break
    else:
        j = -1
    
    # Calculate the minimum mana required to kill the current monster
    if j == i:
        total_mana += k_i[i] + 1
    elif j != -1:
        total_mana += max(k_i[j] - h_j, k_i[i] - h_i) + 1
    else:
        total_mana += k_i[i] + 1

print(total_mana)
