import sys
import suffix_tree

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

strings_trees = [suffix_tree.SuffixTree(string) for string in strings]

occurrences = []
for i, (string_tree, string) in enumerate(zip(strings_trees, strings)):
    occurrences.extend(string_tree.find(text))

min_steps = 0
position_count = {}
for start in set(occurrences):
    position_count[start] = occurrences.count(start)
    min_steps += max(position_count.values())

print(min_steps)
for start in sorted(position_count.keys()):
    for _ in range(position_count[start]):
        index = strings.index(next(string_tree.find(start)))
        print(f"{index} {start}")
