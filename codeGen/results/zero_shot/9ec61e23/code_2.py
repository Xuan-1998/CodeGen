def calculate_mex_sum(n, row1, row2):
    mex_sum = 0
    i = 0
    while i < n:
        # If both rows have 0 in the current column, the MEX is 1
        if row1[i] == '0' and row2[i] == '0':
            mex_sum += 1
            i += 1
        # If both rows have 1 in the current column, the MEX is 0
        # No need to add anything to mex_sum, just move to next column
        elif row1[i] == '1' and row2[i] == '1':
            i += 1
        # If one row has 0 and the other has 1, the MEX is 2
        else:
            mex_sum += 2
            # Skip the next column if it's also a part of the same bi-table with MEX 2
            if i + 1 < n and ((row1[i+1] == '0' and row2[i+1] == '1') or (row1[i+1] == '1' and row2[i+1] == '0')):
                i += 2
            else:
                i += 1
    return mex_sum

def main():
    t = int(input().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(input().strip())  # Read the number of columns
        row1 = input().strip()  # Read the first row
        row2 = input().strip()  # Read the second row
        result = calculate_mex_sum(n, row1, row2)
        print(result)

if __name__ == "__main__":
    main()
