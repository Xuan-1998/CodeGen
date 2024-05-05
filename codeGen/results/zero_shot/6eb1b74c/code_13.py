import sys

t = input().strip()
n = int(input())
used_strings = {}

for i in range(n):
    s = input().strip()

min_steps = float('inf')
steps_taken = 0
current_index = 0

for i in range(len(t)):
    current_index = i
    while current_index < len(t):
        for j in range(n):
            if t[current_index:].startswith(s[j]):
                if s[j] not in used_strings:
                    used_strings[s[j]] = True
                    steps_taken += 1
                    break
                current_index += 1

min_steps = min(min_steps, steps_taken)

if min_steps == float('inf'):
    print(-1)
else:
    for s in sorted(used_strings.keys()):
        print(f"({s}, {current_index})")
