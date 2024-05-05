import sys

# Read input
t = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Create a dictionary to store string indices and lengths
string_indices = {s: i for i, s in enumerate(strings)}

# Store string lengths for efficient matching
string_lengths = [len(s) for s in strings]

# Initialize a dictionary to store start positions of matches
matches = {}

for s in strings:
    for i in range(len(t) - len(s) + 1):
        if t[i:i+len(s)] == s:
            if s not in matches:
                matches[s] = [i]
            else:
                matches[s].append(i)

# Sort occurrences by position
for s, positions in matches.items():
    matches[s] = sorted(positions)

# Initialize variables
m = 0
steps = []

for s, positions in matches.items():
    for position in positions:
        if not steps or steps[-1][1] < position - len(s):
            m += 1
            steps.append((s, position))

# Print output
print(m)
for s, position in steps:
    print(f"{string_indices[s]} {position}")
