import sys
from collections import Counter

n = int(input())
t = input()
strings = [input() for _ in range(n)]

min_steps = float('inf')
used_strings = []

counts = [Counter([c for c in t if s == c]) for s in strings]

for i, (s, count) in enumerate(zip(strings, counts)):
    steps = 0
    while any(count & Counter(t[i:i+len(s)])) > 0:
        steps += 1
        t = t[:i] + 'R' * len(s) + t[i+len(s):]
        for j in range(i, i+len(s)):
            if t[j] == s[0]:
                t = t[:j] + 'R' + t[j+1:]
    min_steps = min(min_steps, steps)
    used_strings.append((i+1, 1))

print(min_steps)

for i, (w, p) in enumerate(used_strings):
    print(f"{w} {p}")
