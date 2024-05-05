# Step 1: Read the input
t = input().strip()
n = int(input())
strings = [input().strip() for _ in range(n)]

# Step 2: Initialize variables
m = -1  # minimum number of steps
steps = []  # list to store the indices of the used strings

# Step 3: Iterate over each string in the set
for i, s in enumerate(strings):
    count = t.count(s)  # count the occurrences of the string
    if count > 0:
        m = min(m, len(s)) if m == -1 else m
        steps.append((i + 1, t.find(s)))  # store the index and position

# Step 4: Determine the minimum number of steps needed
m = len(steps) if m == -1 else m

# Step 5: Print the result
print(m)
if m > 0:
    for j in range(m):
        print(*steps[j])
else:
    print(-1)
