# Step 1: Read the input
N, M, C = map(int, input().split())
upper_radii = list(map(int, input().split()))
lower_radii = list(map(int, input().split()))

# Step 2: Calculate the number of ways to build each sequence length
sequence_counts = [0] * (C + 1)
for r in upper_radii:
    for i in range(C, r - 1, -1):
        sequence_counts[i] += 1

for r in lower_radii:
    for i in range(r, C + 1):
        sequence_counts[i] += 1

# Step 3: Calculate the final answer
answer = [0] * (C + 1)
for i in range(C + 1):
    answer[i] = (sequence_counts[i] * (i - 1)) % (10**9 + 7)

print(*answer, sep=' ')
