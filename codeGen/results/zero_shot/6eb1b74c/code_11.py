import sys

# Read the text and number of strings from standard input
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

# Initialize a dictionary to store the strings as keys and their occurrences in the text as values
string_occurrences = {}

# Iterate over each string
for _ in range(n):
    # Read the next string from standard input
    s = sys.stdin.readline().strip()

    # Store the occurrences of the current string in the text
    for i in range(len(text) - len(s) + 1):
        if text[i:i+len(s)] == s:
            if s not in string_occurrences:
                string_occurrences[s] = [i]
            else:
                string_occurrences[s].append(i)

# Initialize the minimum number of steps and a list to store the steps
min_steps = float('inf')
steps = []

# Iterate over each string and its occurrences
for s, positions in string_occurrences.items():
    # If this is the first string or it's not fully covered by previous strings
    if len(positions) > 0:
        for position in sorted(positions):
            # Find the minimum step that can cover all uncovered positions starting from this position
            current_step = 1
            while position + len(s) <= text.length() and (position + len(s)) % s != 0:
                if (position + len(s)) not in [p for sublist in steps for p in sublist]:
                    current_step += 1
                    position += len(s)
            # Update the minimum number of steps and the steps list
            min_steps = min(min_steps, current_step)
            steps.append([len(string_occurrences) - n + 1, position])

# If it's impossible to color all letters in red, print -1
if min_steps == float('inf'):
    print(-1)

# Otherwise, print the minimum number of steps and the steps list
else:
    print(min_steps)
    for s, positions in string_occurrences.items():
        for position in sorted(positions):
            print(s, position)
