import sys

# Read the first line
text = sys.stdin.readline().strip()

# Read the second line
num_strings = int(sys.stdin.readline())

# Read the strings
strings = []
for _ in range(num_strings):
    strings.append(sys.stdin.readline().strip())

min_steps = float('inf')
steps = 0
used_strings = set()

for i, s in enumerate(strings):
    start = 0
    while start < len(text):
        pos = text.find(s, start)
        if pos != -1:
            steps += 1
            start = pos + 1
        else:
            break
    used_strings.add(i + 1)

if len(text) == sum(1 for c in text if c == 'R'):
    min_steps = min(min_steps, steps)
print(min_steps)

# If it is impossible to color all letters of the text t in red, output -1.
if min_steps == float('inf'):
    print(-1)
else:
    # Print the pairs of indices
    for i, (w, p) in enumerate(zip(used_strings, range(len(text)))):
        if i < len(text):
            print(w, p)
