# Step 1: Read input
n = int(input())
arr = list(map(int, input().split()))

# Step 2: Initialize count of operations
ops = 0

# Step 3: Iterate through array and find minimum number of operations
for i in range(1, n):
    if arr[i] <= arr[i-1]:
        diff = arr[i-1] - arr[i] + 1
        arr[i] += diff // 2
        ops += diff

# Step 4: Print the result
print(ops)
