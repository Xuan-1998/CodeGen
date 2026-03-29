t = input().strip()
n = int(input())
strings = []
for i in range(n):
    strings.append(input().strip())

occurrences = {}
for s in strings:
    start = 0
    while True:
        start = t.find(s, start)
        if start == -1:
            break
        occurrences[start] = s
        start += len(s)

sorted_occurrences = sorted(occurrences.items())
m = 0
used_strings = []
for i, (pos, _) in enumerate(sorted_occurrences):
    if i > 0 and pos != sorted_occurrences[i-1][0] + len(sorted_occurrences[i-1][1]):
        m += 1
        used_strings.append(_)

print(m)
for s in used_strings:
    print(used_strings.index(s) + 1, used_strings.index(s))
