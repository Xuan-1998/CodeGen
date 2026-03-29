# Step 1: Read input
N, M, C = map(int, input().split())
upper_radii = list(map(int, input().split()))
lower_radii = list(map(int, input().split()))

# Step 2: Initialize answer array
answer = [0] * (C + 1)

# Step 3: Iterate over upper and lower radii
for r in set(upper_radii):
    for i in range(C, r - 1, -1):
        answer[i] += 1

for r in set(lower_radii):
    for i in range(r, C + 1):
        answer[i] += 1

# Step 4: Calculate the number of X-sequences
x_sequences = [0] * (C + 1)
for i in range(C + 1):
    x_sequences[i] = (answer[i] * (answer[i - 1] if i > 0 else 1)) % (10**9 + 7)

# Step 5: Print the answer
print(*x_sequences[1:], sep=' ')
