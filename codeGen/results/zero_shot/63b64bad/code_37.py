# Step 1: Read input
n = int(input())  # n represents the length of the sequence
sequence = list(map(int, input().split()))  # sequence is a list of integers representing the sequence

# Step 2: Initialize variables and termination flag
terminate_flag = False  # flag to indicate whether the program terminates or not
y = 0  # initial value of y

for x in range(1, n+1):
    while True:
        # Step 3: Increase both x and y by a_value simultaneously
        x += sequence[x-1]
        y += sequence[x-1]

        # Check termination conditions
        if x <= 0 or x > n:
            terminate_flag = True
            break

        # Step 4: Increase y by a_value while decreasing x by a_value
        y += sequence[x-1]
        x -= sequence[x-1]

    # Print the final value of y and termination flag
    print(y if not terminate_flag else -1)
