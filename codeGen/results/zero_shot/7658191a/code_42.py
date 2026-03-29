# Step 1: Read input
t = int(input())  # number of test cases
for _ in range(t):
    n, k, z = map(int, input().split())  # array size, number of moves, and max consecutive left moves
    arr = list(map(int, input().split()))  # array values

    # Step 2: Initialize variables for the maximum score and current position
    max_score = 0
    pos = 1

    # Step 3: Simulate exactly k moves with no more than z consecutive left moves
    for _ in range(k):
        # Step 4: Check if it's possible to move left or right
        if pos + 1 < n and (pos <= 1 or arr[pos-1] >= arr[pos]):
            pos -= 1
        elif pos > 1:
            pos += 1

        # Step 5: Update the maximum score
        max_score = max(max_score, sum(arr[:pos+1]))

    print(max_score)
