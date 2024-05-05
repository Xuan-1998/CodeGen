import re

text = input()
n = int(input())
strings = [input() for _ in range(n)]

string_occurrences = {}
for i, s in enumerate(strings):
    occurrences = [(j, t.find(s, j)) for j in range(len(text) - len(s) + 1)]
    string_occurrences[s] = occurrences

strings.sort(key=len)

min_steps = float('inf')
used_strings = set()
for s in strings:
    if s in used_strings:
        continue
    used_strings.add(s)
    for j, (start, end) in enumerate(string_occurrences[s]):
        num_chars_colored = end - start + 1
        min_steps = min(min_steps, len(used_strings))

if min_steps == float('inf'):
    print(-1)
else:
    print(min_steps)
    for i, s in enumerate(used_strings):
        print(i + 1, end=' ')
        print(*[(start, end) for start, end in string_occurrences[s]], sep='\n')
