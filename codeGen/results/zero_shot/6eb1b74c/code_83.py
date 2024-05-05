import sys

t = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

min_steps = float('inf')
pairs = []

for i, s in enumerate(strings):
    pos = [i for j in range(len(t)) if t.startswith(s, j)]
    for p in pos:
        if (p, i) not in pairs:  # check if this pair is already in the list
            min_steps = min(min_steps, len(pairs) + 1)
            pairs.append((i, p))

if min_steps == float('inf'):
    print(-1)
else:
    print(min_steps)
    for pair in pairs:
        print(*pair)
