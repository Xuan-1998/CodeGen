n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

k.sort()

def min_mana_required(monster_appearance_time, monster_health):
    min_mana = float('inf')
    for i in range(monster_health, 0, -1):
        if i >= monster_health:
            min_mana = min(min_mana, i)
    return min_mana

total_mana_required = 0
for i in range(n):
    total_mana_required += min_mana_required(k[i], h[i])
print(total_mana_required)
