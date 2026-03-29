import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = []
for i in range(n):
    strings.append(sys.stdin.readline().strip())

min_steps = float('inf')
used_strings = set()
steps = []

for i in range(n):
    used = set()
    for j in range(len(text)):
        found = False
        for k in range(i+1):
            if text[j:j+len(strings[k])].lower() == strings[k].lower():
                found = True
                break
        if found:
            for k in range(i+1):
                used.add(k)
    if len(used) >= n and i not in used_strings:
        min_steps = i + 1
        used_strings = set(list(range(n)))
        steps.append((n, 0))

if min_steps == float('inf'):
    print(-1)
else:
    for i in range(min_steps):
        print(steps[i][0], steps[i][1])
    print(min_steps)
