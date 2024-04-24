def calculate_mex_sum(n, top_row, bottom_row):
    mex_sum = 0
    current_mex = 2  # Initialize to the highest possible MEX

    for i in range(n):
        if top_row[i] == '0' or bottom_row[i] == '0':
            if current_mex == 2:  # Starting a new bi-table or extending with 00
                current_mex = 0
            # If current_mex is 0 or 1, we continue with the same bi-table
        else:  # Both are 1
            if current_mex < 2:  # We found a 11 after a 00 or 01/10, time to start a new bi-table
                mex_sum += current_mex
                current_mex = 2

    # Add the MEX of the last bi-table
    mex_sum += current_mex

    return mex_sum

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Read the number of columns
    top_row = input().strip()  # Read the top row of the bi-table
    bottom_row = input().strip()  # Read the bottom row of the bi-table
    print(calculate_mex_sum(n, top_row, bottom_row))
