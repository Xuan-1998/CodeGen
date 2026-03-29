# Step 1: Read input
N, M, C = map(int, input().split())
upper_radii = list(map(int, input().split()))
lower_radii = list(map(int, input().split()))

# Step 2: Sort radii in ascending order
upper_radii.sort()
lower_radii.sort()

# Step 3: Initialize result array with zeros
result = [0] * (C + 1)

# Step 4: Iterate over upper and lower radii to build X-sequences
for i in range(C):
    count_upper = len([r for r in upper_radii if r <= i]) 
    count_lower = len([r for r in lower_radii if r >= i]) 
    result[i] = (result[i - 1] + count_upper * count_lower) % (10**9 + 7)

print(' '.join(map(str, result)))
