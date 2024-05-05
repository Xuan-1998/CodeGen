n = int(input())
appearances = list(map(int, input().split()))
healths = list(map(int, input().split()))

mana_required = 0
max_damage = 0

for i in range(n):
    if healths[i] > max_damage:
        mana_required += healths[i]
    else:
        mana_required += max_damage + 1
    max_damage = max(max_damage, healths[i])

print(mana_required)
