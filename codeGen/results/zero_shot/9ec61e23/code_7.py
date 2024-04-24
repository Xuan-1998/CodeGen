def calculate_mex_sum(n, top_row, bottom_row):
    mex_sum = 0
    current_mex = 0  # This will store the MEX of the current segment

    for i in range(n):
        if top_row[i] == '1' and bottom_row[i] == '1':
            # If both bits are 1, the MEX is 2 and we make a cut
            mex_sum += 2
            current_mex = 0  # Reset the MEX for the new segment
        else:
            # If either bit is 0, the MEX is at most 1, we can continue the current segment
            current_mex = max(current_mex, int(top_row[i]) + int(bottom_row[i]))

    # Add the MEX of the last segment
    mex_sum += current_mex

    return mex_sum

# Read number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    n = int(input().strip())  # Number of columns in the bi-table
    top_row = input().strip()  # Top row of the bi-table
    bottom_row = input().strip()  # Bottom row of the bi-table
    
    # Calculate and output the maximal sum of MEX
    print(calculate_mex_sum(n, top_row, bottom_row))
