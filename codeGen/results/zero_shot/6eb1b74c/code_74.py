# Step 1: Read input
t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]

# Step 2: Create a dictionary to store the strings and their occurrences in the text
string_occurrences = {s: [] for s in strings}
for i, c in enumerate(t):
    for s in strings:
        if t[i:i+len(s)] == s:
            string_occurrences[s].append(i)

# Step 3: Initialize variables to keep track of the minimum number of steps and the pairs of indices
min_steps = float('inf')
step_pairs = []

# Step 4: Iterate through the text and find the minimum number of steps needed to color all letters in red
for i, c in enumerate(t):
    for s in strings:
        if t[i:i+len(s)] == s:
            string_occurrences[s].append(i)
            min_steps = min(min_steps, len(string_occurrences[s]))
            step_pairs.extend([(j+1, i) for j in range(len(string_occurrences[s]))])

# Step 5: Print the result
if min_steps == float('inf'):
    print(-1)
else:
    print(min_steps)
    for pair in step_pairs:
        print(*pair)
