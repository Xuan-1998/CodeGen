n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

k.sort()

mana = 0
last_health = 0
total_damage = 0

for i in range(n):
    while mana < k[i] - last_health:
        mana += 1
    total_damage += max(k[i], last_health)
    last_health = h[i]

print(total_damage)
