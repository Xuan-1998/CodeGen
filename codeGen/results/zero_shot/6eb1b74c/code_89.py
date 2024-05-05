import sys
import collections

t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]

def build_suffix_tree(s):
    tree = collections.defaultdict(list)
    for i, c in enumerate(reversed(s)):
        tree[c].append(i)
    return tree

def find_occurrences(t, s):
    occurrences = {}
    for si in strings:
        occurrences[si] = []
        for i in range(len(t) - len(si) + 1):
            if t[i:i+len(si)] == si:
                occurrences[si].append(i)
    return occurrences

def color_all_letters(occurrences):
    min_steps = 0
    for si, indices in occurrences.items():
        if len(indices) > 0:
            min_steps += len(indices)
    return min_steps

min_steps = color_all_letters(find_occurrences(t, strings))
print(min_steps)

if min_steps > 0:
    for j, (si, indices) in enumerate(sorted(occurrences.items()), 1):
        if len(indices) > 0:
            for i, index in enumerate(indices):
                print(j, index + 1 - len(si))
else:
    print(-1)
