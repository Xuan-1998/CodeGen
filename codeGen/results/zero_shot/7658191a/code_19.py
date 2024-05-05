python
# Step 1: Read input
n, k, z = map(int, input().split())
arr = list(map(int, input().split()))

# Step 2: Initialize variables
max_score = 0
left_moves = 0

# Step 3: Iterate over the array
for i in range(1, n):
    # If we can make a move to the left, calculate the score
    if left_moves < z:
        max_score += arr[i-1]
        left_moves += 1
    # If we cannot make a move to the left, move to the right
    else:
        max_score += arr[i]

# Step 4: Make k moves
for _ in range(k):
    if left_moves > 0:
        max_score += arr[n-1 - left_moves]
        left_moves -= 1
    else:
        max_score += arr[n-1]

print(max_score)
