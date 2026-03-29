# Read input
t = input()
n = int(input())
strings = [input() for _ in range(n)]

# Create a dictionary to store the positions of each string in the text
string_positions = {s: [] for s in strings}
for i, c in enumerate(t):
    for s in strings:
        if s.startswith(c):
            string_positions[s].append(i)

# Sort the strings by their lengths (shortest to longest)
strings.sort(key=len)

# Initialize the minimum number of steps and the list of pairs
min_steps = 0
pairs = []

# Iterate over the strings, trying to color all letters in red
for s in strings:
    while string_positions[s]:
        position = string_positions[s].pop(0)
        # Check if coloring this substring will cover any remaining substrings
        for other_s in strings:
            if other_s != s and string_positions[other_s]:
                new_position = string_positions[other_s].pop(0)
                if position <= new_position:
                    break  # we can't color this substring, backtrack!
        else:
            min_steps += 1
            pairs.append((s, position))

# Print the result
print(min_steps)
for s, p in pairs:
    print(f"{s} {p}")
