import sys
import faster_fs as fs

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

fsts = []
for s in strings:
    fst = fs.FS(s)
    fsts.append((len(s), fst))

occurrences = []
for _, fst in fsts:
    pos_occurrences = [(pos, len(s)) for s, pos in zip(fst.prefixes(), range(len(text))) if text.startswith(s)]
    occurrences.append(pos_occurrences)

sorted_occurrences = [sorted(occurrences[i], key=lambda x: x[0]) for i in range(n)]

steps = []
current_pos = 0
for i, occs in enumerate(sorted_occurrences):
    for pos, _ in occs:
        if current_pos < pos:
            break
        steps.append((i + 1, pos))
        current_pos = pos

print(len(steps))

for w, p in steps:
    print(w, p)
