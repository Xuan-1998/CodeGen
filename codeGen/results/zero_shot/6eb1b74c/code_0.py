import sys
from collections import Counter
import math

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

string_counts = Counter({s: text.count(s) for s in strings})

min_steps = math.ceil(sum(string_counts.values()) / max(len(s) for s in strings))

steps = []
for _ in range(min_steps):
    max_count = 0
    best_string = None
    for string, count in string_counts.items():
        if count > max_count:
            max_count = count
            best_string = string
    string_counts[best_string] -= len(best_string)
    steps.append((n + 1 - strings.index(best_string), best_string))

print(min_steps)

for step in steps:
    print(*step)
