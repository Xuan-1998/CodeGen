n = int(input())
appearances = list(map(int, input().split()))
healths = list(map(int, input().split()))

appearances.sort()

min_mana_needed = 0
max_damage = 0

for i in range(len(appearances)):
    max_damage = max(max_damage, healths[i])
    min_mana_needed += max_damage

print(min_mana_needed)
