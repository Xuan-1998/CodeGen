import sys

def solve():
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    string_occurrences = {}
    for i, s in enumerate(strings):
        if s not in string_occurrences:
            string_occurrences[s] = []
        for j, c in enumerate(s):
            if c in t and (t.index(c) + len(s) <= len(t)):
                string_occurrences[s].append(t.index(c))

    minimum_steps = 0
    steps_taken = 0
    steps = []

    while True:
        used_strings = set()
        for s, indices in string_occurrences.items():
            if not any(i is None for i in indices):
                for index in indices:
                    t = list(t)
                    t[index:index+len(s)] = ['R' if c == s[0] else 'B' for c in s]
                    t = ''.join(t)
                used_strings.add(s)
        if all(indices is None for indices in string_occurrences.values()):
            break
        steps_taken += 1

    print(steps_taken)

    for i, (s, indices) in enumerate(string_occurrences.items()):
        if s in used_strings:
            print(f'{i+1} {indices[0]}')

solve()
