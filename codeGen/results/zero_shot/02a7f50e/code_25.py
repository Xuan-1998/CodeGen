import sys

n = int(sys.stdin.readline())
beams = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beams.append((a, b))

beams.sort(key=lambda x: x[1], reverse=True)

destroyed = 0
max_position = 0
for a, b in beams:
    if a > max_position:
        max_position = a
    else:
        destroyed += b
print(destroyed)

new_beam = int(sys.stdin.readline())
print(new_beam)
