import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

m = float('inf')
steps = []

for s in strings:
    pos = text.find(s)
    if pos != -1:
        m = min(m, 1 + pos // len(s))
        steps.append((strings.index(s) + 1, pos))

steps_needed = m
for w, p in steps:
    if p > len(s):
        steps_needed += 1

print(steps_needed)
for w, p in sorted(steps):
    print(w, p)
