# Step 1: Read the input array
N = int(input())
arr = list(map(int, input().split()))

# Step 2: Initialize variables for counting operations
ops = 0
prev_val = arr[0]

# Step 3: Iterate through the array to find minimum number of operations
for val in arr[1:]:
    if val <= prev_val:
        ops += (prev_val - val) + 1
    prev_val = val

print(ops)
