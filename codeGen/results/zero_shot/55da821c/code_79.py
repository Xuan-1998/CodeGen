# Step 1: Read input
n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, x = map(float, input().split())
    plants.append((species, x))

# Step 2: Sort plants by position
plants.sort(key=lambda x: x[1])

# Step 3: Initialize the minimum number of replants and current section index
replants = 0
current_section = 1

# Step 4: Iterate over the plants and assign them to sections
for plant in plants:
    if plant[0] != current_section:
        replants += 1
        current_section += 1

print(replants)
