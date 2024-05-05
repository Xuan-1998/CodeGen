# Step 1: Read input
n = int(input())
monsters = []
for _ in range(n):
    k, h = map(int, input().split())
    monsters.append((k, h))

# Step 2: Sort monsters by appearance time
monsters.sort()

# Step 3: Initialize minimum mana required to kill all monsters
min_mana = 0

# Step 4: Iterate over each monster
for k, h in monsters:
    # Step 5: Calculate the mana required to kill this monster
    mana_required = max(1, h)
    min_mana += mana_required

print(min_mana)
