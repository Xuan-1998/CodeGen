# Step 1: Read the input
t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]

# Step 2: Preprocess the strings
string_set = set(strings)
strings.sort(key=len)

# Step 3: Initialize variables to keep track of the solution
min_steps = float('inf')
steps = []
used_strings = set()

# Step 4: Try to color the text using the given strings
for i, string in enumerate(strings):
    while True:
        pos = t.find(string)
        if pos == -1:
            break
        used_strings.add(i)
        t = t[:pos] + '*' * len(string) + t[pos + len(string):]
    
    # Step 5: Update the minimum number of steps and the solution
    min_steps = min(min_steps, i + 1 if pos == -1 else i)
    steps.extend([(i, j) for j in range(len(t)) if t[j] != '*'])

# Step 6: Print the result
print(min_steps)
for step in steps:
    print(*step)
