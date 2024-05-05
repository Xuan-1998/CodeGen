# Read the input
n = int(input())
monsters = list(map(int, input().split()))
healths = list(map(int, input().split()))

# Sort the monsters by their appearance time
monsters.sort()

# Initialize the minimum mana required to kill all monsters
min_mana = 0

for i in range(len(monsters)):
    # The damage of the spell at the current second is at least the health of the current monster
    min_mana = max(min_mana, monsters[i] - healths[i] + 1)

print(min_mana)
