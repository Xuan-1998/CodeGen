def calculate_mex(column):
    if column == "00":
        return 0
    elif "0" in column:
        return 1
    else:
        return 2

def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n = int(input().strip())  # Number of columns
        top_row = input().strip()
        bottom_row = input().strip()
        
        mex_sum = 0
        current_mex = 0
        
        for i in range(n):
            column = top_row[i] + bottom_row[i]
            mex = calculate_mex(column)
            if mex == 0:
                # Cut the bi-table here and start a new one
                mex_sum += current_mex
                current_mex = 0
            else:
                # Update the current_mex if we see a column with MEX 2
                current_mex = max(current_mex, mex)
        
        # Add the MEX of the last sub bi-table
        mex_sum += current_mex
        
        print(mex_sum)

if __name__ == "__main__":
    main()
