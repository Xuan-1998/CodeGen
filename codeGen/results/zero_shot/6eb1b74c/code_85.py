# Step 1: Read input
t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]

# Step 2: Initialize variables
m = 0
used_strings = set()

# Step 3: Iterate over strings and text
for i, s_i in enumerate(s):
    while True:
        found = False
        pos = t.find(s_i)
        if pos != -1:
            for j in range(len(s_i)):
                t = t[:pos+j] + "#" + t[pos+j]
            m += 1
            used_strings.add(i)
            break

# Step 4: Print result
if len(used_strings) == n:
    print(m)
    for i, s_i in enumerate(s):
        if i in used_strings:
            print(f"({i+1}, {t.find(s_i)})")
else:
    print(-1)
