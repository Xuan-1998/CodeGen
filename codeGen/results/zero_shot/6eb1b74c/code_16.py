import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

min_steps = float('inf')
pairs = []

for i, s in enumerate(strings):
    steps = 0
    pos = -1
    for j, c in enumerate(text):
        if text[j:j+len(s)] == s:
            steps += 1
            pos = j
            pairs.append((i+1, pos))
    min_steps = min(min_steps, steps)

print(min_steps if min_steps != float('inf') else -1)
if min_steps != float('inf'):
    for pair in pairs:
        print(*pair)
