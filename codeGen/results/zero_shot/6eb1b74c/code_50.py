import sys
import re

# Read the text
text = sys.stdin.readline().strip()
# Read the number of strings
n = int(sys.stdin.readline())
# Read the strings
strings = [sys.stdin.readline().strip() for _ in range(n)]

string_lengths = [(len(s), i) for i, s in enumerate(strings)]
string_lengths.sort()
strings = [s for _, s in string_lengths]

occurrences = []
for i, s in enumerate(strings):
    matches = [(m.start(), m.end()) for m in re.finditer(s, text)]
    occurrences.append(matches)

min_steps = 0
result = []

for i, matches in enumerate(occurrences):
    for match in matches:
        if min_steps >= len(result):
            break
        min_steps += 1
        result.append((i, match[0]))

print(min_steps)
for i, match in enumerate(result):
    print(f"{match[0]} {match[1]}")
