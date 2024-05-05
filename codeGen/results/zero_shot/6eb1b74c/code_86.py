import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

string_lengths = {s: len(s) for s in strings}

# Implement a suffix tree construction algorithm here
suffix_tree = construct_suffix_tree(text)

occurrences = {}
for s, length in string_lengths.items():
    occurrences[s] = []
    for node in suffix_tree:
        if node.label == s and len(node.path) >= length:
            # Add the occurrence to the list
            occurrences[s].append((node.path.index(s), node.path))

steps = 0
current_streak = 1
for i, occurrence in enumerate(occurrences.values()):
    if i > 0:
        previous_occurrence = occurrences[list(occurrences.keys())[i-1]]
        # Check if the current occurrence is part of a streak with the previous occurrence
        if occurrence[0] - previous_occurrence[-1][0] == 1:
            current_streak += 1
        else:
            steps += current_streak // 2
            current_streak = 1
steps += current_streak // 2

print(steps)
for i, (string_index, occurrences_list) in enumerate(occurrences.items()):
    for j, occurrence in enumerate(occurrences_list):
        if j > 0:
            print(f"{i+1} {j}")
