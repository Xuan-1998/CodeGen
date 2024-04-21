import sys

def calculate_mex_sum(n, top_row, bottom_row):
    last_both_zero = -1
    last_both_one = -1
    mex_sum = 0
    
    for i in range(n):
        if top_row[i] == '0' and bottom_row[i] == '0':
            # The MEX for any segment ending here is at least 1.
            last_both_zero = i
        elif top_row[i] == '1' and bottom_row[i] == '1':
            # The MEX for any segment ending here is at least 2.
            last_both_one = i
            mex_sum += 2  # We can add 2 immediately because we must cut before this column.
        else:
            # The MEX for any segment ending here could be 0, 1, or 2.
            # We add 1 if we are forced to cut before this column due to previous '11'.
            mex_sum += 1 if last_both_one >= last_both_zero else 0
            
    return mex_sum

def main():
    t = int(sys.stdin.readline().strip())  # Read the number of test cases
    for _ in range(t):
        n = int(sys.stdin.readline().strip())  # Read the number of columns for this test case
        top_row = sys.stdin.readline().strip()  # Read the top row binary string
        bottom_row = sys.stdin.readline().strip()  # Read the bottom row binary string
        result = calculate_mex_sum(n, top_row, bottom_row)
        print(result)

if __name__ == "__main__":
    main()
