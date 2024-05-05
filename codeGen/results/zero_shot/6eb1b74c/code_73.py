import sys

t = input().strip()
n = int(input())
s = []
for i in range(n):
    s.append(input().strip())

text = [ord(c) for c in t]
strings = []
for s in s:
    strings.append([ord(c) for c in s])

occurrences = []
for i, s in enumerate(strings):
    for j in range(len(text) - len(s) + 1):
        if text[j:j+len(s)] == s:
            occurrences.append((i, j))

steps = 0
occurrences.sort(key=lambda x: x[1])
for i, (s_index, pos) in enumerate(occurrences):
    if i > 0 and occurrences[i-1][1] + len(strings[occurrences[i-1][0]]) <= pos:
        steps += 1

print(steps)
if steps == -1:
    print(-1)
else:
    for i, (s_index, pos) in enumerate(occurrences):
        print(f"{s_index} {pos}")
