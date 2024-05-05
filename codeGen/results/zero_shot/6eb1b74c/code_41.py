t = input()
n = int(input())
strings = []
for i in range(n):
    strings.append(input())

trie = {}
for s in strings:
    pattern = re.compile(s)
    trie[s] = pattern

matches = {}
for s, pattern in trie.items():
    matches[s] = [m.start() for m in pattern.finditer(t)]

def min_steps(matches):
    min_steps = 0
    prev_end = 0
    for s, pos in matches.items():
        end = max(pos)
        while prev_end < end:
            min_steps += 1
            prev_end = end
            end = min(e for e in pos if e > prev_end)

print(min_steps(matches))
for j, (w, p) in enumerate(sorted((w, p) for w, ps in matches.items() for p in ps)):
    print(w, p)
