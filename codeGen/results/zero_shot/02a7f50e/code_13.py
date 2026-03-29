import sys

n = int(sys.stdin.readline().strip())
beams = []
for _ in range(n):
    pos, power = map(int, sys.stdin.readline().strip().split())
    beams.append((pos, power))

beams.sort()

max_power = max(power for _, power in beams)

destroyed_beams = 0
min_destroyed = float('inf')

for i, (pos, _) in enumerate(beams):
    destroyed = (beams[i-1][0] if i > 0 else -sys.maxsize) // (pos + 1)
    min_destroyed = min(min_destroyed, destroyed)

print(min_destroyed)
