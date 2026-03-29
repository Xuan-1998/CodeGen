# Read input
n, x = map(int, input().split())

# Convert x to string for easier manipulation
x_str = str(x)

# Calculate the current length of x's decimal representation
curr_len = len(x_str)

if curr_len >= n:
    # If the current length is already equal to or greater than n, return 0
    print(0)
else:
    # Initialize the minimum number of operations needed
    min_ops = -1

    for i in range(curr_len, n):
        # For each digit in x's decimal representation, check if it can be used as a multiplier
        for j in range(10):
            new_x = int(x_str + str(j))  # Create the new value of x by appending the digit j
            new_len = len(str(new_x))  # Calculate the length of the new decimal representation

            if new_len == n:  # If the new length is equal to n, update min_ops and break
                min_ops = i + 1
                break

        if min_ops != -1:
            break

    print(min_ops)
