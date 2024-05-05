import sys

n = int(sys.stdin.readline())
positions = []
powers = []

for i in range(n):
    pos, pow = map(int, sys.stdin.readline().split())
    positions.append(pos)
    powers.append(pow)

powers.sort(reverse=True)

destroyed = 0
for i in range(n):
    while destroyed > 0 and powers[i] >= powers[destroyed - 1]:
        destroyed -= 1

    destroyed += 1

print(destroyed)

new_pos = int(sys.stdin.readline())
new_pow = int(sys.stdin.readline())

while destroyed > 0 and new_pow >= powers[destroyed - 1]:
    destroyed -= 1

print(destroyed)
