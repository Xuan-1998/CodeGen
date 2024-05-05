import sys

def read_input():
    n = int(input())
    s = input()
    return n, s

n, s = read_input()

# Step 1: Find all possible pairs of substrings
pairs = []
for i in range(n):
    for j in range(i+1, n):
        pairs.append((s[:i+1], s[i+1:j+1]))

# Step 2: Calculate the bitwise OR of each pair and store them in a set to remove duplicates
or_values = set()
for p in pairs:
    val1 = int(p[0], 2)
    val2 = int(p[1], 2)
    or_value = val1 | val2
    or_values.add(or_value)

# Step 3: Find the maximum possible value without leading zeroes
max_or_value = max(str(bin(x))[2:] for x in or_values)

print(max_or_value)
