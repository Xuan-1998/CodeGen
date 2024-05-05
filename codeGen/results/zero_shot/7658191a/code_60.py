# Step 1: Read input
t = int(input())  # Number of test cases
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Step 2: Sort the array in descending order
    arr.sort(reverse=True)
    
    # Step 3: Initialize maximum score and current position
    max_score = 0
    curr_pos = 1
    
    # Step 4: Loop through k moves
    for _ in range(k):
        if z > 0:
            # Try to move left, add value at previous index to score
            new_score = arr[curr_pos - 2] + max_score
            if new_score > max_score and curr_pos - 2 >= 1:
                max_score = new_score
                curr_pos -= 1
                z -= 1
            else:
                # Move right, add value at next index to score
                max_score += arr[curr_pos]
                curr_pos += 1
        else:
            # No more moves left, move right and add value at next index to score
            max_score += arr[curr_pos]
            curr_pos += 1
    
    # Step 5: Print the maximum score
    print(max_score)
