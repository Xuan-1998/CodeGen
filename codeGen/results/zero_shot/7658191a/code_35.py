# Step 1: Read the input
t = int(input()) # number of test cases
for _ in range(t):
    n, k, z = map(int, input().split()) # n is the size of array, k is the number of moves, z is the maximum number of left moves
    a = list(map(int, input().split())) # array of positive integers

    # Step 2: Initialize variables
    max_score = [0] * (k + 1) # maximum score for each number of moves
    left_moves = [0] * (k + 1) # number of left moves for each number of moves

    # Step 3: Fill the dp table using dynamic programming
    for i in range(1, k + 1):
        if i <= z:
            max_score[i] = a[0]
            left_moves[i] = 1
        else:
            max_score[i] = max(max_score[i - 1], a[0])
            left_moves[i] = 1

        for j in range(1, n):
            if i > z or (i == z and j < z + 1):
                # move to the right
                if j <= k:
                    score = max_score[j - 1] + a[j]
                    if score > max_score[i]:
                        max_score[i] = score
                        left_moves[i] = left_moves[j - 1] + (0 if i == z else 1)
            elif i > 1 and j >= k:
                # move to the left
                score = max_score[i - 2] + a[j]
                if score > max_score[i]:
                    max_score[i] = score
                    left_moves[i] = left_moves[i - 2] + (0 if i == z else 1)

    print(max_score[k])
