t = input().strip()
n = int(input())
string_occurrences = {}
for i in range(n):
    si = input().strip()
    start = 0
    while True:
        pos = t.find(si, start)
        if pos == -1:
            break
        string_occurrences[i] = string_occurrences.get(i, []) + [(pos, pos + len(si) - 1)]
        start = pos + 1

m = 0
covered_chars = set()
for si in string_occurrences:
    for start, end in sorted(string_occurrences[si]):
        if any(c >= start and c <= end for c in covered_chars):
            m += 1
            covered_chars.update(range(start, end + 1))

if covered_chars != set(range(len(t))):
    print(-1)
else:
    print(m)
    for j, (start, end) in enumerate(sorted([(pos, pos + len(si) - 1) for si in string_occurrences.values()])):
        print(f"{j+1} {start}")
