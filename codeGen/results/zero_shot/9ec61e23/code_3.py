def mex(s):
    if s == "00":
        return 0
    elif s == "01" or s == "10":
        return 1
    else: # s == "11"
        return 2

def solve(n, top_row, bottom_row):
    # Initialize the sum of MEX values
    mex_sum = 0
    # Initialize the previous MEX value to -1 (to represent no previous value)
    prev_mex = -1

    # Iterate over each column
    for i in range(n):
        # Compute the MEX for the current column
        current_mex = mex(top_row[i] + bottom_row[i])
        # If the current MEX is different from the previous MEX, we make a cut
        if current_mex != prev_mex:
            mex_sum += current_mex
            prev_mex = current_mex

    return mex_sum

def main():
    # Read the number of test cases
    t = int(input())
    # Process each test case
    for _ in range(t):
        # Read the number of columns in the bi-table
        n = int(input())
        # Read the two binary strings
        top_row = input().strip()
        bottom_row = input().strip()
        # Solve the test case and output the result
        print(solve(n, top_row, bottom_row))

if __name__ == "__main__":
    main()
