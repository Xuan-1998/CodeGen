import sys
from suffix_tree import SuffixTree

n = int(sys.stdin.readline())
text = sys.stdin.readline().strip()
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().strip())

text_suffix_tree = SuffixTree(text)
occurrences = []
for s in strings:
    occurrence_nodes = text_suffix_tree.traverse(s)
    occurrences.append([(node.position, node.length) for node in occurrence_nodes])

steps = 0
used_strings = set()
for s, occurrences in zip(strings, occurrences):
    used_strings.add(s)
    steps += len(occurrences)

if len(used_strings) != n:
    print(-1)
else:
    print(steps)
    for s, occurrences in zip(strings, occurrences):
        for position, length in occurrences:
            print(position, end=' ')
        print()
