# Step 1: Define the function
def max_score(n, k, z, arr):
    # Step 2: Initialize the score
    score = 0
    
    # Step 3: Initialize the move counter
    moves = 0
    
    # Step 4: Iterate through the array
    for i in range(1, n + 1):
        # Step 5: Check if we can make a move to the left
        if moves < z and (i - 2 >= 1 or moves == 0):
            # Make a move to the left and add the value at index i-1 to the score
            score += arr[i-1]
            moves += 1
        else:
            # If we can't make a move to the left, make a move to the right
            score += arr[i]
        
        # Step 6: Check if we have made k moves
        if moves == k:
            break
    
    return score

# Step 7: Read input and calculate maximum score for each test case
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(max_score(n, k, z, arr))
