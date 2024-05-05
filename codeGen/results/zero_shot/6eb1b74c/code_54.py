import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

min_steps = 0
used_strings = {}
positions = {}

for i, s in enumerate(strings):
    pos = [i for i in range(len(text)) if text[i:].startswith(s)]
    positions[s] = pos
    used_strings[s] = 0

for s, pos in positions.items():
    used_strings[s] += len(pos)

min_steps = sum(used_strings.values())

if min_steps > 0:
    print(-1)
else:
    print(min_steps)

for s, pos in positions.items():
    if len(pos) == used_strings[s]:
        for i in range(len(pos)):
            print(f"{s} {pos[i]}")
