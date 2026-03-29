import sys

def calculate_mana(appearance_times, healths):
    total_mana = 0
    prev_damage = 0
    for t, h in zip(appearance_times, healths):
        damage_needed = h - 1
        if prev_damage > 0 and prev_damage >= damage_needed:
            total_mana += prev_damage
            prev_damage -= damage_needed
        else:
            total_mana += damage_needed
            prev_damage = max(1, prev_damage + 1)
    return total_mana

t = int(input())
for _ in range(t):
    n = int(input())
    appearance_times = list(map(int, input().split()))
    healths = list(map(int, input().split()))
    print(calculate_mana(appearance_times, healths))
